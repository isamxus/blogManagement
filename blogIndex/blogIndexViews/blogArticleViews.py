from django.views.decorators.csrf import csrf_exempt
from ..models import ArticleDetail, IndexImageManagement, CommentDetail
from ..base import IndexSqlHandler
from myblogdjango.base import DataSqlHandler

#添加文章
@csrf_exempt
def createArticleHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ArticleDetail, request, 'add')

#更新文章
@csrf_exempt
def updateArticleHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ArticleDetail, request, 'update')

#获取一篇文章
@csrf_exempt
def getSingleArticleHandler(request):
	return IndexSqlHandler.Get_Single_Handler(IndexSqlHandler,ArticleDetail, request)

#删除文章
@csrf_exempt
def deleteArticleHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ArticleDetail, request, 'delete', extra={
			'ConnectModel':[
				{
					'ForeignModel': IndexImageManagement,
					'ForeignKey': 'ConnectArticleID'
				},
				{
					'ForeignModel': CommentDetail,
					'ForeignKey': 'parentArticleID'
				}
			] 
		})


#获取文章列表 (不分页)
@csrf_exempt
def getArticleListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ArticleDetail, request, 'getlist')

#获取文章列表 （分页）
@csrf_exempt
def getArticlePageListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ArticleDetail, request, 'getpagelist')