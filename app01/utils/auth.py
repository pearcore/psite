from rest_framework import exceptions
from app01 import models
from rest_framework.authentication import BaseAuthentication

class FirstAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass

    def authenticate_header(self,request):
        pass

class PsiteAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.headers['token']
        except Exception as e:
            token = ''
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj :
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user , token_obj)
    def authenticate_header(self,request):
        #return 'Basic realm= "api"'
        pass