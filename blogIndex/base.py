from myblogdjango.base import DataSqlHandler
from django.shortcuts import get_object_or_404

class IndexSqlHandler(DataSqlHandler):
	#获取文章详情
	def Get_Single_Handler(self, ModelClass, request, extra={}):
		try:
			extra = self.loginStatus(self, request, extra)
			requestData = self.RequestHandler(self, request)
			primary_key = self.return_primary_key(self, ModelClass)
			extra['mustFields'] = [primary_key]
			response = self.mustFieldsCheck(self, ModelClass, requestData, extra)
			if type(response).__name__ != 'dict':
				return response
			SingleData = get_object_or_404(ModelClass, pk=requestData[primary_key])
			SingleData.articleViews += 1
			SingleData.save(update_fields=['articleViews'])
			SingleData = ModelClass.objects.filter(**response).values()[0]
			return self.ResponseHandler(self, True, SingleData, extra=extra)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False, e)