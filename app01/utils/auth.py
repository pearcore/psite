from django.http import JsonResponse
from app01 import models
from rest_framework import exceptions

class FirstAuthtication(object):
    def authenticate(self, request):
        pass
    def authenticate_header(self,val):
        pass


class Authtication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        #在restframework内部会将两个字段赋值给request，以供后面使用。
        return (token_obj.user,token_obj)
    def authenticate_header(self,val):
        pass