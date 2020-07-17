from django.http import JsonResponse
from app01 import models
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

class FirstAuthtication(BaseAuthentication):
    def authenticate(self, request):
        pass
    def authenticate_header(self,val):
        pass


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data['token']
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        #在restframework内部会将两个字段赋值给request，以供后面使用。
        return (token_obj.user,token_obj)

        #return None (下一个认证执行，我不管了。)
        #raise exceptions.AuthenticationFailed('用户认证失败') 认证失败
        #return (token_obj.user,token_obj) 认证通过，返回认证的用户信息和token信息。


    def authenticate_header(self,val):
        pass

class PSiteAuthentication(BaseAuthentication):
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