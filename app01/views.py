from rest_framework.views import APIView
from django.http import JsonResponse
from psite.LHStand import LHKit
from app01 import models
from rest_framework import serializers

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

from app01.utils.throttle import PSiteIPThrottle, PSiteUserThrottle
class AuthView(APIView): #用于用户登录

    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    #throttle_classes = [Visit2Throttle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            user = request.data["username"] #request._request.POST.get('username')
            password = request.data["password"] #request._request.POST.get('password')
            print("lalalala2!")
            #print(password)
            #print(request.body)
            obj = models.UserInfo.objects.filter(username=user,password=password).first()
            if not obj:
                ret['code'] = 1001 
                ret['data'] = "登录失败"
                ret['msg'] = "用户名或密码错误！"
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
    }}
from app01.utils.permission import SVIPPermission,NONSVIPPermission

class OrderView(APIView): #订单相关业务
    #authentication_classes = [Authtication,]
    #authentication_classes = []
    permission_classes = [SVIPPermission,]
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        # token = request._request.GET.get('token')
        # if not token :
        #     ret['code'] = 900
        #     ret['msg'] = '用户没登录'
        #     return JsonResponse(ret)
        try:
            ret ['data'] = ORDER_DICT
            ret ['user'] = request.user.username
            ret ['userType'] = request.user.user_type
            

        except Exception as e:
            pass
        return JsonResponse(ret)

# class UserInfoSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     type1 = serializers.CharField(source="user_type")
#     type2 = serializers.CharField(source="get_user_type_display")
#     glala = serializers.CharField(source="group.title")
#     rls = serializers.SerializerMethodField()

#     def get_rls(self,row):
#         role_obj_list = row.roles.all()
#         ret = []
#         for item in role_obj_list:
#             ret.append ({"id":item.id,"title":item.title})
#         return ret
class MyField(serializers.CharField):
    def to_representation(self,value):
        return "XXXXX"

class UserInfoSerializer(serializers.ModelSerializer):
    oooo = serializers.CharField(source="get_user_type_display")
    rls = serializers.SerializerMethodField()
    xl = MyField(source="username")
    class Meta:
        model = models.UserInfo
        #fields = "__all__"
        fields = ["id",'username','password','oooo','rls','group','xl']
        #extra_kwargs = {'group':{'source':'group.title'},}
    def get_rls(self,row):
        role_obj_list = row.roles.all()
        ret = []
        for item in role_obj_list:
            ret.append ({"id":item.id,"title":item.title})
        return ret
    

class UserInfoView(APIView): #订单相关业务
    #authentication_classes = [Authtication,]
    #authentication_classes = []
    permission_classes = [NONSVIPPermission,]
    
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        userinfos  =  models.UserInfo.objects.all()
        ud = UserInfoSerializer(instance=userinfos,many = True)
        #dt = LHKit.objects_to_JSON(userinfos)
        try:
            ret ['data'] = ud.data

        except Exception as e:
            pass
        return JsonResponse(ret)

from rest_framework.versioning import URLPathVersioning
class UsersView(APIView):
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    #versioning_class = URLPathVersioning
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        u1 = request.versioning_scheme.reverse(viewname='qqq',request=request)
        #from django.urls import reverse
        #u2 = reverse(viewname='qqq',kwargs={'ver':2})
        ret ['data'] = u1 #request.version 
        return JsonResponse(ret)

class DjangoView(APIView):
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    #versioning_class = URLPathVersioning
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        ret ['data'] = "3333" 
        return JsonResponse(ret)

class ParserView(APIView):
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    #versioning_class = URLPathVersioning
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        ret ['data'] = request.data['test2']
        return JsonResponse(ret)


class RolesSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.CharField()


class RolesView(APIView):
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    #versioning_class = URLPathVersioning
    def post(self,request,*args,**kwargs):
        ret = LHKit.LHResult()
        #方式1
        #roles = models.Role.objects.all().values('id' , 'title')
        #roles = list(roles)
        #方式2
        #roles = models.Role.objects.all()
        #ser = RolesSerializer(instance=roles,many = True)

        #方式3
        #roles = models.Role.objects.all()
        #mydata = LHKit.objects_to_JSON(roles)

        ret['data'] = mydata
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