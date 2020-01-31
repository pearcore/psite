from django.conf.urls import url
from app01 import views 

urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/auth/$' , views.AuthView.as_view(), name = 'uuu'),
]