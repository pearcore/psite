from rest_framework.views import APIView
from django.http import JsonResponse
from psite.LHStand import LHKit
from app01 import models

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class AuthView(APIView): #用于用户登录
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            user = request._request.POST.get('username')
            password = request._request.POST.get('password')

            obj = models.UserInfo.objects.filter(username=user,password=password).first()
            if not obj:
                ret['code'] = 1001 
                ret['data'] = "登录失败"
            else:
                ret['code'] = 10000
                ret['data'] = "登录成功"
                token = md5(user)
                ret['token'] = token
                #有就更新，没有就创建
                models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = '请求异常！'

        return JsonResponse( ret ) 

ORDER_DICT = {
    1:{
        'name':'媳妇',
        'age':18,
        'gender':'男',
        'content':'.......'
    },
    2:{
        'name':'金毛',
        'age':5,
        'gender':'',
        'content':'一条狗'
    }
}

from rest_framework import exceptions
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

class OrderView(APIView): #订单相关业务
    authentication_classes = [Authtication,]

    def get(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        # token = request._request.GET.get('token')
        # if not token :
        #     ret['code'] = 900
        #     ret['msg'] = '用户没登录'
        #     return JsonResponse(ret)
        try:
            ret ['data'] = ORDER_DICT
            ret ['user'] = request.user.username
            #ret ['tokenobj'] = request.auth
        except Exception as e:
            pass
        return JsonResponse(ret)

    

# from django.shortcuts import render,HttpResponse
# import json
# from psite.LHStand import LHKit
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt,csrf_protect
# # Create your views here.

# def users(request):
#     user_list = ["Test","dkdkdk"]
#     rt = LHKit.LHResult()
#     rt['data'] = user_list
#     return HttpResponse( json.dumps( rt ) )

# from django.views import View

# class StudentsView(View):
#     #@method_decorator(csrf_exempt)
#     def dispatch(self, request , *args, **kwargs):
#         print('before')
#         ret = super(StudentsView,self).dispatch(request , *args , **kwargs)
#         print('after')
#         return ret 
    
#     def get(self,request , *args, **kwargs):
#         user_list = ["dddd","aaaaa"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )
#     def post(self,request , *args, **kwargs):
#         user_list = ["Post","Post"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )
#     def put(self,request , *args, **kwargs):
#         user_list = ["Method","这个是PUT方法"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ,ensure_ascii=False) )

#     def delete(self,request , *args, **kwargs):
#         user_list = {"Method":"delete"}
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )
# from rest_framework import exceptions
# class MyAuthentication(object):
#     def authenticate(self,request):
#         token = request._request.GET.get('token')
#         if not token :
#             raise exceptions.AuthenticationFailed("认证失败鸟！")
#         return ('Alex',None)
#     def authenticate_header(self,val):
#         pass

# from rest_framework.views import APIView
# class DogView(APIView):
#     authentication_classes = [MyAuthentication]
#     def get(self,request , *args, **kwargs):
#         user_list = ["dddd","aaaaa"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )
#     def post(self,request , *args, **kwargs):
#         user_list = ["Post","Post"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )
#     def put(self,request , *args, **kwargs):
#         user_list = ["Method","这个是PUT方法"]
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ,ensure_ascii=False) ,status = 204 )

#     def delete(self,request , *args, **kwargs):
#         user_list = {"Method":"delete"}
#         rt = LHKit.LHResult()
#         rt['data'] = user_list
#         return HttpResponse( json.dumps( rt ) )