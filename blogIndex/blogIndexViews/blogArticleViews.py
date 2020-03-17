from django.views.decorators.csrf import csrf_exempt
from ..models import ArticleDetail
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
	return DataSqlHandler.Data_Handler(DataSqlHandler,ArticleDetail, request, 'getsingle')

#删除文章
@csrf_exempt
def deleteArticleHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ArticleDetail, request, 'delete')


#获取文章列表
@csrf_exempt
def getArticleListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ArticleDetail, request, 'getlist')