from django.http import JsonResponse
from rest_framework.views import APIView
from app01 import models

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5( bytes(user , encoding='utf-8'))
    m.update ( bytes(ctime , encoding='utf-8' ))
    return m.hexdigest

class AuthView(APIView):
    def post(self, request , *args, **kwargs):
        try: 
            ret = { 'code':1000, 'msg':'成功!'}
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            print (user)
            obj = models.UserInfo.objects.filter(user_name=user,password=pwd).first()
            if not obj :
                ret['code'] = 1001
                ret['msg'] = '没成功!'
            token = md5(user)
            models.UserToken.objects.update_or_create(user = obj , defaults = {'token':token})

        except Exception as e:
           pass
        
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


