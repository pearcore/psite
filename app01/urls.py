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

    url(r'^(?P<ver>[v1|v2|v3]+)/users/$',views.UsersView.as_view()), #本链接里面允许的
]
