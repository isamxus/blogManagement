from django.views.decorators.csrf import csrf_exempt
from ..models import ParamsSettings,ParamsContent
from blogIndex.models import ArticleDetail, CommentDetail
from myblogdjango.base import DataSqlHandler

#添加参数
@csrf_exempt
def createDetailHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsContent, request, 'add')

#更新参数
@csrf_exempt
def updateDetailHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsContent, request, 'update')

#更新参数
@csrf_exempt
def getSingleDetailHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsContent, request, 'getsingle')

#删除参数
@csrf_exempt
def deleteDetailHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ParamsContent, request, 'delete', extra={
			'ConnectModel':[
				{
					'ForeignModel': ArticleDetail,
					'ForeignKey': 'articleCagetoryID',
					'children': [
						{
							'ForeignModel': CommentDetail,
							'ForeignKey': 'parentArticleID',
							'DeleteAll': True,
							'lock': ['0001'],
							'lockkey': 'detailParentParamCode'
						}
					]
				},
			] 
		})


#获取参数列表
@csrf_exempt
def getDetailListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ParamsContent, request, 'getlist')
