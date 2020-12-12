from rest_framework.views import APIView
from rest_framework.response import Response
from tools.LHStand import LHKit
from league import models

from league.utils.throttle import PSiteIPThrottle,PSiteUserThrottle
from league.utils.auth import Authtication

class LoginView(APIView): 
    authentication_classes = []
    throttle_classes = [PSiteIPThrottle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            user = request.data["mobile"] #request._request.POST.get('username')
            password = request.data["password"] #request._request.POST.get('password')
            obj = models.PlayerLogin.objects.filter(mobile=user,password=password).first()
            if not obj:
                ret['code'] = 1001 
                ret['msg'] = "Mobile or Password wrong！"
            else:
                ret['code'] = 10000
                ret['msg'] = "Login success!"
                token = LHKit.md5(user)
                ret['data'] = token
                #有就更新，没有就创建
                models.PlayerToken.objects.update_or_create(user=obj,defaults={'token':token})
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = 'Request abnormal! ' 

        return Response( ret ) 

class ClubListView(APIView): 
    authentication_classes = [Authtication]
    throttle_classes = [PSiteUserThrottle]
    #throttle_classes = [Visit2Throttle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            #request.user.id

            leagues  =  models.Club.objects.all().order_by('-points','-goals_for')
            ret["data"] = LHKit.objects_to_JSON(leagues)
            # user = request.data["mobile"] #request._request.POST.get('username')
            # password = request.data["password"] #request._request.POST.get('password')
            # obj = models.PlayerLogin.objects.filter(mobile=user,password=password).first()
            # if not obj:
            #     ret['code'] = 1001 
            #     ret['msg'] = "Mobile or Password wrong！"
            # else:
            #     ret['code'] = 10000
            #     ret['msg'] = "Login success!"
            #     token = LHKit.md5(user)
            #     ret['data'] = token
            #     #有就更新，没有就创建
            #     models.PlayerToken.objects.update_or_create(user=obj,defaults={'token':token})
            
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = 'Request abnormal! ' 

        return Response( ret ) 