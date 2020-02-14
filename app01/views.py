from django.http import JsonResponse
from rest_framework.views import APIView
from app01 import models
from rest_framework import exceptions
from psite.LHStand import LHKit
from django.db.models import Q
from app01.utils.auth import FirstAuthentication,PsiteAuthentication
from app01.utils.permission import SVIPPermission,NormalPermission
from app01.utils.throttle import PSiteIPThrottle,PSiteUserThrottle
import json
from django.urls import reverse
from rest_framework.parsers import JSONParser,FormParser
#from rest_framework.versioning import URLPathVersioning

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


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5( bytes(user , encoding='utf-8'))
    m.update ( bytes(ctime , encoding='utf-8' ))
    return m.hexdigest()

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
    authentication_classes = []
    permission_classes = []
    throttle_classes = [PSiteIPThrottle,]
    #versioning_class = URLPathVersioning
    parser_classes = [ JSONParser,]
    def post(self, request , *args, **kwargs):
        try: 
            ret = LHKit.LHResult()
            user = request.data['username'] #request._request.POST.get('username')
            pwd = request.data['password'] #request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(user_name=user,password=pwd).first()
            print (obj)
            if not obj :
                ret['code'] = 900
                ret['msg'] = '查无此人!'
            else:
                token = md5(user)
                models.UserToken.objects.update_or_create(user = obj , defaults = {'token':token})
                ret ['data'] = token
                #ret ['code'] = 998
                #ret ['msg'] = '我就说它不成功！'
                ret ['Ver'] = request.version
                #print (request.body)
            # if request.version == 'v2' :
            #     ret ['ADD'] = '新添加一点东西!'
            # u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
            # u2 = reverse(viewname = 'uuu',kwargs= {'version':request.version})


        except Exception as e:
            ret['code'] = 997
            ret['msg'] = '出现了异常,请联系管理员'
        
        return JsonResponse(ret)

class OrderView(APIView):
    permission_classes = []
    def post(self, request , *args, **kwargs):
        ret = LHKit.LHResult()
        try:
            ret['data'] = Order_Dict
        except Exception as e :
            pass
        return JsonResponse(ret)

from rest_framework import status
class UserInfoView(APIView):
    def post(self, request , *args, **kwargs):
        ret = LHKit.LHResult()
        try:
            ret['data'] = LHKit.object_to_JSON( request.user )
        except Exception as e :
            pass
        return JsonResponse(ret)

class UsersView(APIView):
    permission_classes = [SVIPPermission,]
    def post(self, request , *args, **kwargs):
        ret = LHKit.LHResult()
        users = models.UserInfo.objects.filter(~Q(user_name=''))
        jsUsers = LHKit.objects_to_JSON(users)
        ret ['data'] = jsUsers
        return JsonResponse(ret)
   
class ParserView(APIView):
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle,]
    #parser_classes = [ JSONParser,FormParser,]
    def post(self,request , *args, **kwargs):
        #print(request.headers['token'])
        rtJson = LHKit.LHResult()
        rtJson['data'] = request.data['age']
        return JsonResponse(rtJson)

from rest_framework import serializers

class RoleSer(serializers.Serializer):
    title = serializers.CharField(label='zzz')

class RolesView(APIView):
    permission_classes = [SVIPPermission,]
    throttle_classes = [PSiteUserThrottle,]
    parser_classes = [ JSONParser,]
    def post(self,request , *args, **kwargs):
        roles = models.UserRole.objects.all()
        ser = RoleSer(instance = roles , many = True)

        rtJson = LHKit.LHResult()
        rtJson['data'] = ser.data
        return JsonResponse(rtJson)

class UserInfoSer0(serializers.Serializer):
    Name = serializers.CharField(source='user_name')
    pwd = serializers.CharField(source='password')
    itType = serializers.CharField(source='user_type')
    stType = serializers.CharField(source='get_user_type_display')
    gp = serializers.CharField(source='group.title')
    role = serializers.CharField(source='role.all')
    role2 = serializers.SerializerMethodField()
    def get_role2(self , row):
        allRoles = row.role.all()
        ret = []
        for temp in allRoles :
            ret.append(
                {
                    "id":temp.id,
                    "title":temp.title
                }
            )
        return  ret

class LHCharfield(serializers.CharField):
    def to_representation(self,value):
        print (value)
        return "something"

class UserInfoSer1(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        #fields = '__all__'
        fields = ['id','user_name','role2','stType','group_name','gogogo']
        #extra_kwargs = {'group':{'source':'group.title'},}
    gogogo = LHCharfield(source= "user_name")
    stType = serializers.CharField(source='get_user_type_display')
    role2 = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()
    def get_role2(self , row):
        allRoles = row.role.all()
        ret = []
        for temp in allRoles :
            ret.append(
                {
                    "id":temp.id,
                    "title":temp.title
                }
            )
        return  ret
    def get_group_name(self , row):
        return row.group.title

class UserInfoSer2(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        depth = 1

class UserInfosView(APIView):
    def post(self,request , *args, **kwargs):
        users = models.UserInfo.objects.all()
        serU = UserInfoSer2(instance=users,many = True)
        rtJson = LHKit.LHResult()
        rtJson['data'] = serU.data
        return JsonResponse(rtJson)

