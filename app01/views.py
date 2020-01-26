from django.http import JsonResponse
from rest_framework.views import APIView
from app01 import models
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from django.core import serializers
from psite.LHStand import LHKit
from django.db.models import Q
import json

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5( bytes(user , encoding='utf-8'))
    m.update ( bytes(ctime , encoding='utf-8' ))
    return m.hexdigest

Order_Dict = {
    1:{
        'Name':'手纸',
        'Number':3,
        'Content':'...',
    },
    2:{
        'Name':'水杯',
        'Number':4,
        'Content':'water cup',
    },
    3:{
        'Name':'维生素C',
        'Number':10,
        'Content':'CCCCC',
    },
    4:{
        'Name':'test',
        'Number':40,
        'Content':'testtest',
    },
    
}

class AuthView(APIView):
    def post(self, request , *args, **kwargs):
        try: 
            ret = { 'code':1001, 'msg':'成功!'}
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            print (user)
            obj = models.UserInfo.objects.filter(user_name=user,password=pwd).first()
            if not obj :
                ret['code'] = 1001
                ret['msg'] = '没成功!'
            token = md5(user)
            models.UserToken.objects.update_or_create(user = obj , defaults = {'token':token})
            ret ['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '出现了异常,请联系管理员'
        
        return JsonResponse(ret)

class PsiteAuthentication(object):
    def authenticate(self, request):
        token = request._request.POST.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj :
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user , token_obj)
    def authenticate_header(self,request):
        pass


class OrderView(APIView):
    authentication_classes = [ PsiteAuthentication, ]
    def post(self, request , *args, **kwargs):
        ret = {
            "code":1000,
            "msg":"成功!",
            "data":"",
        }
        try:
            ret['data'] = Order_Dict
        except Exception as e :
            pass
        return JsonResponse(ret)

class UserInfoView(APIView):
    authentication_classes = [ PsiteAuthentication, ]
    def post(self, request , *args, **kwargs):
        ret = LHKit.LHResult()
        try:
            ret['data'] = LHKit.object_to_JSON( request.user )
        except Exception as e :
            pass
        return JsonResponse(ret)

class UsersView(APIView):
    def post(self, request , *args, **kwargs):
        ret = LHKit.LHResult()
        users = models.UserInfo.objects.filter(~Q(user_name=''))
        jsUsers = LHKit.objects_to_JSON(users)
        ret ['data'] = jsUsers
        return JsonResponse(ret)

# import json
# from django.shortcuts import render,HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.views import APIView

# # Create your views here.
# @csrf_exempt
# def users(request):
#     user_list = ["test01", "test02"]
#     return HttpResponse( json.dumps(user_list))

# from django.views import View

# @method_decorator(csrf_exempt,name="dispatch")
# class StudentsView(APIView):
#     # @method_decorator(csrf_exempt)
#     # def dispatch(self , request, *args , **kwargs ):
#     #     return super(StudentsView,self).dispatch(request, *args, **kwargs)

#     def get(self, request,*args, **kwargs):
#         return HttpResponse("Get")
#     def post(self, request,*args, **kwargs):
#         return HttpResponse("Post")

# # from django.views import View
# #@method_decorator(csrf_exempt,name="dispatch")
# from rest_framework import exceptions
# class LHAuthentication(object):
#     def authenticate(self ,request):
#         token = request._request.GET.get('token')
#         if not token :
#             raise exceptions.AuthenticationFailed('认证失败鸟~')
#         return (token,None)
#     def authenticate_header (self,val):
#         pass

# from django.views import View
# from rest_framework.views import APIView
# class DogsView(APIView):
#     authentication_classes = [LHAuthentication,]
#     def post(self, request,*args, **kwargs):
#         print (request)
#         print (request.user)
#         self.dispatch
#         return HttpResponse("sdsfsfsdfsfsGet" + request.user)


