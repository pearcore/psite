from django.conf.urls import url
from app01 import views 

urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/auth/$' , views.AuthView.as_view(), name = 'uuu'),
    url(r'^(?P<version>[v1|v2]+)/order/$' , views.OrderView.as_view(), name = 'order'),
    url(r'^(?P<version>[v1|v2]+)/django/$' , views.DjangoView.as_view(), name = 'ddd'),
    url(r'^(?P<version>[v1|v2]+)/parser/$' , views.ParserView.as_view()),
]