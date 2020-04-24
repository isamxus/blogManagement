from django.conf.urls import url
 
from .UsersViews import UserManagementViews
 
urlpatterns = [
	#用户管理api
	url(r'^User/Create/$', UserManagementViews.createUserHandler, name='createUserHandler'),
	url(r'^User/Update/$', UserManagementViews.updateUserHandler, name='updateUserHandler'),
	url(r'^User/UpdateAuth/$', UserManagementViews.updateUserAuthHandler, name='updateUserAuthHandler'),
	#url(r'^User/GetSingle/$', UserManagementViews.getSingleUserHandler, name='getSingleUserHandler'),
	url(r'^User/GetPageList/$', UserManagementViews.getUsersPageListHandler, name='getUsersPageListHandler'),
	url(r'^User/Delete/$', UserManagementViews.deleteUserHandler, name='deleteUserHandler'),
	url(r'^User/Login/$', UserManagementViews.userLoginHandler, name='userLoginHandler'),
	url(r'^UserImage/Upload/$', UserManagementViews.User_ImageUpload_Handler, name='User_ImageUpload_Handler'),
	url(r'^User/CheckLoginStatus/$', UserManagementViews.UserCheckStatusHandler, name='UserCheckStatusHandler'),
	url(r'^User/ChangePassword/$', UserManagementViews.changePasswordHandler, name='changePasswordHandler'),
]