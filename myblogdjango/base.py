import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms import model_to_dict
from rest_framework.authtoken.models import Token
from django.db.models import Q
from django.db.models import F
from .authCheck import AuthTokenHandler
#基础类
class DataSqlHandler(object):
	#处理后的PostContent
	PostContent = None
	#缓存请求数据
	requestData = None
	#判断key是否存在于dict中并返回value
	def Is_In_Dict(self, key, dict, type={}):
		return dict[key] if (dict and key in dict.keys() and dict[key]) else type

	#请求成功返回
	def SuccessMsg(self, success={}, extra={}):
		return dict({
			'status':True,
			'Msg': '成功！！！'
		}, **(success if (success) else {'success': '请求成功！！！'}), **(self.Is_In_Dict(self, 'extraFields', extra, {})))

	#请求失败返回
	def FailedMsg(self, err={}, extra={}):
		return dict({
			'status':False,
			'Msg': '失败！！！'
		}, **(err if(err) else {'err': '服务器发生错误，请联系管理员！！！'}), **(self.Is_In_Dict(self, 'extraFields', extra, {})))

	#验证登录状态
	def loginStatus(self, requestData, extra):
		Data = self.RequestHandler(self, requestData, True)
		needUserInfo = self.Is_In_Dict(self, 'needUserInfo', extra, False)
		extra['extraFields'] = self.Is_In_Dict(self, 'extraFields', extra, {})
		if needUserInfo == True:
			result = AuthTokenHandler.check_login_status(AuthTokenHandler, Data, True)
			if result['IsLogin']:
				Token = AuthTokenHandler.resign_Token(AuthTokenHandler, Data['Token'])
				extra['extraFields'].update(Token=Token)
			extra['extraFields'].update(IsLogin=result['IsLogin'])
			extra['extraFields'].update(UserInfo=result['UserInfo'])
		else:
			result = AuthTokenHandler.check_login_status(AuthTokenHandler, Data)
			if result == True:
				Token = AuthTokenHandler.resign_Token(AuthTokenHandler, Data['Token'])
				extra['extraFields'].update(Token=Token)
			extra['extraFields'].update(IsLogin=result)
		return extra
	#对请求数据进行处理
	def RequestHandler(self, request, returnOther=False):
		requestData = json.loads(json.dumps(request.POST))
		if returnOther:
			if not 'PostContent' in requestData.keys():
				requestData['PostContent'] = {}
			return requestData
		return json.loads(requestData['PostContent']) if('PostContent' in requestData.keys()) else {}

	#对请求进行响应
	def ResponseHandler(self, status, obj={}, success={}, err={}, extra={}):
		return JsonResponse(dict({'PostContent':obj if(obj) else []}, **(self.SuccessMsg(self, success, extra=extra) if(status) else self.FailedMsg(self, err, extra=extra))))

	#返回主键字段
	def return_primary_key(self, ModelClass):
		for field in ModelClass._meta.fields:
			if field.primary_key:
				return field.attname
		return
	#取得Model类中所有字段并生成列表
	def Put_Fields_to_List(self, ModelClass, extra):
		att_list = []
		ignoreList = self.Is_In_Dict(self, 'ignoreFields', extra, [])
		for field in ModelClass._meta.fields:
			if field.attname in ignoreList:
				continue
			att_list.append(field.attname)
		return att_list

	#序列化数据库查询数据
	def SerializeData(self, Data, ModelClass, extra):
		#Data = json.loads(serializers.serialize('json',Data))
		ret_list = []
		ret_Fields = ModelClass()
		for batch in Data:
			obj = {}
			for key in self.Put_Fields_to_List(self, ModelClass, extra):
				obj[key] = batch[key]
			ret_list.append(obj)
		return ret_list

	#验证必传字段并返回筛选条件
	def mustFieldsCheck(self, ModelClass, Data, extra):
		_filter = {}
		must_field_list = self.Is_In_Dict(self, 'mustFields', extra, [])
		for field in must_field_list:
			if field not in Data.keys() or not Data[field]:
				return self.ResponseHandler(self, False, err={'err':("缺少%s参数！！！")%field}, extra=extra)
			if Data[field]:
				_filter[field] = Data[field]
		return _filter
	#根据筛选条件与数据库匹配
	def mapDatabase(self, ModelClass, _filter, extra):
		checkData = ModelClass.objects.filter(**_filter).values()																				
		if checkData:
			return self.ResponseHandler(self, True, self.SerializeData(self, checkData, ModelClass, extra), success={'IsOK': self.Is_In_Dict(self, 'success', extra, True)}, extra=extra)
		return self.ResponseHandler(self, False, err={
				'err': self.Is_In_Dict(self, 'err', extra, '无匹配数据！！！')
			}, extra=extra)

	#对返回数据的处理
	def Handle_Return_Data(self, ModelClass, prikey, value, extra):
		try:
			#是否需要返回更新后的数据
			needReturnData = self.Is_In_Dict(self, 'needReturnData', extra, False)
			#忽略返回的字段
			ignoreList = self.Is_In_Dict(self, 'ignoreFields', extra, [])
			_filter = {}
			_filter[prikey] = value
			#定义返回的数据
			SingleData = None
			if needReturnData:
				SingleData = ModelClass.objects.filter(**_filter).values()[0]
				for field in ignoreList:
					del SingleData[field]
			return SingleData
		except Exception as e:
			print(e)
		

	#添加数据
	def Create_Data_Handler(self, ModelClass, PostData, extra):
		try:
			Create_Data = ModelClass()
			primary_key = self.return_primary_key(self, ModelClass)
			for field in PostData:
				if primary_key == field:
					continue
				setattr(Create_Data, field, PostData[field])
			Create_Data.save()
			return self.ResponseHandler(self, True, extra=extra)
		except Exception as e:
			return self.ResponseHandler(self, False, extra=extra)

	#更新数据
	def Updata_Data_Handler(self, ModelClass, PostData, extra):
		try:
			primary_key = self.return_primary_key(self, ModelClass)
			UpdataData = get_object_or_404(ModelClass, pk=PostData[primary_key])
			#只需要更新的字段集合
			onlyUpdate = self.Is_In_Dict(self, 'onlyUpdate', extra, False)
			#自定义在extraFields里返回的字段
			ReturnFields = self.Is_In_Dict(self, 'ReturnFields', extra, False)
			extra['extraFields'] = self.Is_In_Dict(self, 'extraFields', extra, {})
			for field in PostData:
				if onlyUpdate and field not in onlyUpdate:
					continue
				setattr(UpdataData, field, PostData[field])
			UpdataData.save()
			SingleData = self.Handle_Return_Data(self, ModelClass, primary_key, PostData[primary_key], extra)
			if ReturnFields:
				extra['extraFields'][ReturnFields] = SingleData
				SingleData = None
			return self.ResponseHandler(self, True, SingleData, extra=extra)
		except Exception as e:
			return self.ResponseHandler(self, False, extra=extra)

	#获取单个数据
	def Getsingle_Data_Handler(self, ModelClass, PostData, extra):
		try:
			primary_key = self.return_primary_key(self, ModelClass)
			extra['mustFields'] = [primary_key]
			response = self.mustFieldsCheck(self, ModelClass, PostData, extra)
			if type(response).__name__ != 'dict':
				return response
			SingleData = ModelClass.objects.filter(**response).values()[0]
			return self.ResponseHandler(self, True, SingleData, extra=extra)
		except Exception as e:
			return self.ResponseHandler(self, False, extra=extra)

	#递归删除数据
	def Recursion_Delete_Handler(self, arr, PostData, primary_key):
		try:
			for model in arr:
				ForeignModel = self.Is_In_Dict(self, 'ForeignModel', model, False)
				ForeignKey = self.Is_In_Dict(self, 'ForeignKey', model, False)
				DeleteAll = self.Is_In_Dict(self, 'DeleteAll', model, False)
				children = self.Is_In_Dict(self, 'children', model, False)
				lock = self.Is_In_Dict(self, 'lock', model, [])
				lockkey = self.Is_In_Dict(self, 'lockkey', model, False)
				if DeleteAll and lockkey and (PostData[lockkey] in lock):
					ForeignModel.objects.all().delete()
				if ForeignKey and ForeignModel and not DeleteAll:
					_filter = {}
					_filter[ForeignKey] = PostData[primary_key]
					ForeignModel.objects.filter(**_filter).delete()
				if children:
					return self.Recursion_Delete_Handler(self, children, PostData, primary_key)
		except Exception as e:
			print(e)
	#删除数据
	def Delete_Data_Handler(self, ModelClass, PostData, extra):
		try:
			primary_key = self.return_primary_key(self, ModelClass)
			ConnectModel = self.Is_In_Dict(self, 'ConnectModel', extra, False)
			extra['mustFields'] = [primary_key]
			response = self.mustFieldsCheck(self, ModelClass, PostData, extra)
			if type(response).__name__ != 'dict':
				return response
			get_object_or_404(ModelClass, pk=PostData[primary_key]).delete()
			if ConnectModel:
				self.Recursion_Delete_Handler(self, ConnectModel, PostData, primary_key)
			return self.ResponseHandler(self, True, extra=extra)
		except Exception as e:
			return self.ResponseHandler(self, False ,extra=extra)

	#获取列表数据（不分页）
	def GetList_Data_Handler(self, ModelClass, PostData, extra):
		try:
			_filter = self.Is_In_Dict(self, 'filter', PostData)
			_OrderBy = self.Is_In_Dict(self, '_OrderBy', PostData, 'CreateTime')
			PostContent = ModelClass.objects.filter(**_filter).order_by(_OrderBy).values()
			PostContent = self.SerializeData(self, PostContent, ModelClass, extra)
			return self.ResponseHandler(self, True, PostContent, extra=extra)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False, extra=extra)
	#获取列表数据（分页）
	def GetPageList_Data_Handler(self, ModelClass, PostData, extra):
		try:
			_filter = self.Is_In_Dict(self, 'filter', PostData, {})
			_OrderBy = self.Is_In_Dict(self, '_OrderBy', PostData, 'CreateTime')
			_PageSize = self.Is_In_Dict(self, 'PageSize', PostData, False)
			_PageNumber = self.Is_In_Dict(self, 'PageNumber', PostData, False)
			if _PageSize and _PageNumber:
				if (isinstance(_PageSize, int) and _PageSize > 0) and (isinstance(_PageNumber, int) and _PageNumber > 0):
					PostContent = ModelClass.objects.filter(**_filter).order_by(_OrderBy).values()
					count = PostContent.count()
					PostContent = PostContent[((_PageNumber-1) * _PageSize):((_PageNumber) * _PageSize)]	
					PostContent = self.SerializeData(self, PostContent, ModelClass, extra)
					return self.ResponseHandler(self, True, {
							'Items': PostContent,
							'PageSize': _PageSize,
							'PageNumber': _PageNumber,
							'TotalItems': count
						}, extra=extra)
				else:
					return self.ResponseHandler(self, False, err={'err':'PageSize或PageNumber必须为正整数！！！'}, extra=extra)
			else:
				return self.ResponseHandler(self, False, err={'err':'缺少PageSize或PageNumber参数！！！'}, extra=extra)

		except Exception as e:
			return self.ResponseHandler(self, False, e, extra=extra)
	#批量插入数据
	def Batch_Insert_Data(self, ModelClass, PostData, extra):
		try:
			List_To_Insert = [] 
			extra['Data'] = self.Is_In_Dict(self, 'Data', extra, False)
			if not isinstance(extra['Data'], list):
				return self.ResponseHandler(self, False, err={'err':'extra["Data"]必须为list！！！'}, extra=extra)
			requestData = PostData if not extra['Data'] else extra['Data']
			for item in requestData:
				exp = ModelClass()
				for field in item.keys():
					setattr(exp, field, item[field])
				List_To_Insert.append(exp)
			ModelClass.objects.bulk_create(List_To_Insert)
			return self.ResponseHandler(self, True, extra=extra)
		except Exception as e:
			print(e)

	def Data_Handler(self, ModelClass, requestData, type, extra={}):
		try:
			extra = self.loginStatus(self, requestData, extra)
			PostData = self.RequestHandler(self, requestData)
			if type=='add':
				return self.Create_Data_Handler(self, ModelClass, PostData, extra)
			if type=='update':
				return self.Updata_Data_Handler(self, ModelClass, PostData, extra)
			if type=='getsingle':
				return self.Getsingle_Data_Handler(self, ModelClass, PostData, extra)
			if type=='delete':	
				return self.Delete_Data_Handler(self, ModelClass, PostData, extra)
			if type=='getlist':
				return self.GetList_Data_Handler(self, ModelClass, PostData, extra)
			if type=='getpagelist':
				return self.GetPageList_Data_Handler(self, ModelClass, PostData, extra)
		except Exception as e:
			print(e)

