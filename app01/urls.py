from django.conf.urls import url
from app01 import views 

urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/auth/$' , views.AuthView.as_view(), name = 'uuu'),
    url(r'^(?P<version>[v1|v2]+)/order/$' , views.OrderView.as_view(), name = 'order'),
    url(r'^(?P<version>[v1|v2]+)/userinfo/$' , views.UserInfoView.as_view(), name = 'userinfo'),
    url(r'^(?P<version>[v1|v2]+)/users/$' , views.UsersView.as_view(), name = 'users'),
    url(r'^(?P<version>[v1|v2]+)/parser/$' , views.ParserView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/roles/$' , views.RolesView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/userinfos/$' , views.UserInfosView.as_view()),
    #url(r'^(?P<version>[v1|v2]+)/group/(?P<pk>\d+)$' , views.GroupView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/group/(?P<pk>\d+)$' , views.GroupView.as_view(),name='gp')


]