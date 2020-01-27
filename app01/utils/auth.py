from rest_framework import exceptions
from app01 import models

class FirstAuthentication(object):
    def authenticate(self, request):
        pass

    def authenticate_header(self,request):
        pass

class PsiteAuthentication(object):
    def authenticate(self, request):
        token = request._request.POST.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj :
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user , token_obj)
    def authenticate_header(self,request):
        pass