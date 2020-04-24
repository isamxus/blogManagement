from django.views.decorators.csrf import csrf_exempt
from ..models import Users
from ..base import UserSqlHandler
from myblogdjango.filesHandle import FilesHandler
from blogIndex.models import IndexImage
#添加用户
@csrf_exempt
def createUserHandler(request):
	return UserSqlHandler.Create_User_Handler(UserSqlHandler, Users, request, 'add')

#用户更新
@csrf_exempt
def updateUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'update', extra={
			'onlyUpdate': ['UserName', 'UserHeadImg', 'Jurisdiction'],
			'needReturnData': True,
			'ignoreFields': ['PassWord'],
			'ReturnFields': 'UserInfo'
		})


#更新用户权限
@csrf_exempt
def updateUserAuthHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'update', extra={
			'onlyUpdate': ['Jurisdiction'],
			'ignoreFields': ['PassWord'],
		})
#获取一个用户信息
'''@csrf_exempt
def getSingleUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'getsingle')'''

#删除用户
@csrf_exempt
def deleteUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'delete')

#获取用户列表（分页）
@csrf_exempt
def getUsersPageListHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'getpagelist', extra={
			'ignoreFields': ['PassWord']
		})

#用户登录
@csrf_exempt
def userLoginHandler(request):
	return UserSqlHandler.User_Login_Handler(UserSqlHandler, Users, request, extra = {
				'ignoreFields': ['PassWord'],
				'mustFields': ['UserName', 'PassWord'],
				'err': '用户名未注册或密码错误！！！',
				'success': True
			})

#获取用户登录状态
@csrf_exempt
def UserCheckStatusHandler(request):
	return UserSqlHandler.User_CheckStatus_Handler(UserSqlHandler, Users, request)

#用户头像上传
@csrf_exempt
def User_ImageUpload_Handler(request):
	return FilesHandler.Upload_Files_Handler(FilesHandler, IndexImage, request)

#修改用户密码
@csrf_exempt
def changePasswordHandler(request):
	return UserSqlHandler.Change_PassWord_Handler(UserSqlHandler, Users, request, extra={
			'onlyUpdate': ['PassWord'],
			'mustFields': ['UserName', 'PassWord', 'user_id'],
			'err': '修改用户密码失败！！！'
		})