#     url(r'^admin/' , admin.site.urls),
#     url(r'^app01api/v1/auth/$' , views.AuthView.as_view()),
#     url(r'^app01api/v1/order/$' , views.OrderView.as_view()),
#     url(r'^app01api/v1/userinfo/$' , views.UserInfoView.as_view()),
    
# ]
from django.conf.urls import url,include
from app01 import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'xxxxx',views.View1View)
#router.register(r'rt',views.View1View)

urlpatterns = [
    url(r'^(?P<ver>[v1|v2|v3]+)/auth/$' , views.AuthView.as_view()),
    url(r'^(?P<ver>[v1|v2|v3]+)/order/$' , views.OrderView.as_view()),
    url(r'^(?P<ver>[v1|v2|v3]+)/userinfo/$' , views.UserInfoView.as_view()),

    url(r'^(?P<ver>[v1|v2|v3]+)/users/$',views.UsersView.as_view(),name='qqq'), #本链接里面允许的
    url(r'^(?P<ver>[v1|v2|v3]+)/django/$',views.DjangoView.as_view(),name='rrr'), 
    url(r'^(?P<ver>[v1|v2|v3]+)/parser/$',views.ParserView.as_view()), 
    url(r'^(?P<ver>[v1|v2|v3]+)/roles/$',views.RolesView.as_view()), 
    url(r'^(?P<ver>[v1|v2|v3]+)/group/(?P<xxx>\d+)$',views.GroupView.as_view(),name='gp'), 
    url(r'^(?P<ver>[v1|v2|v3]+)/usergroup/$',views.UserGroupView.as_view(),name='ugp'),
    url(r'^(?P<ver>[v1|v2|v3]+)/pager1/$',views.Pager1View.as_view()),
    #url(r'^(?P<ver>[v1|v2|v3]+)/view1/$',views.View1View.as_view()),
    # url(r'^(?P<ver>[v1|v2|v3]+)/view1/$',views.View1View.as_view({'get':'list','post':'create'})),
    # #url(r'^(?P<ver>[v1|v2|v3]+)/view1/\.(?P<format>\w+)$',views.View1View.as_view({'get':'list','post':'create'})),

    # url(r'^(?P<ver>[v1|v2|v3]+)/view1/(?P<pk>\d+)$',views.View1View.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),



    # url(r'^(?P<ver>[v1|v2|v3]+)/lhtestapi/$' , views.LHTestApi.as_view()),
    #url(r'^' , include(router.urls))

    url(r'^(?P<ver>[v1|v2|v3]+)/cttest/$',views.CtTestView.as_view()),
    url(r'^(?P<ver>[v1|v2|v3]+)/cttest2/$',views.CtTest2View.as_view()),


]
