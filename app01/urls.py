#     url(r'^admin/' , admin.site.urls),
#     url(r'^app01api/v1/auth/$' , views.AuthView.as_view()),
#     url(r'^app01api/v1/order/$' , views.OrderView.as_view()),
#     url(r'^app01api/v1/userinfo/$' , views.UserInfoView.as_view()),
    
# ]
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'^(?P<ver>[v1|v2|v3]+)/auth/$' , views.AuthView.as_view()),
    url(r'^(?P<ver>[v1|v2|v3]+)/order/$' , views.OrderView.as_view()),
    url(r'^(?P<ver>[v1|v2|v3]+)/userinfo/$' , views.UserInfoView.as_view()),

    url(r'^(?P<ver>[v1|v2|v3]+)/users/$',views.UsersView.as_view(),name='qqq'), #本链接里面允许的
    url(r'^(?P<ver>[v1|v2|v3]+)/django/$',views.DjangoView.as_view(),name='rrr'), 
    url(r'^(?P<ver>[v1|v2|v3]+)/parser/$',views.ParserView.as_view()), 
    url(r'^(?P<ver>[v1|v2|v3]+)/roles/$',views.RolesView.as_view()), 
    

]
