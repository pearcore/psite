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
            user = request.data["mobile"] 
            password = request.data["password"] 
            obj = models.PlayerLogin.objects.filter(mobile=user,password=password).first()
            obj2 = models.PlayerInfo.objects.filter(player_login=obj).first()
            
            if not obj:
                ret['code'] = 800 
                ret['msg'] = "Mobile or Password wrong！"
            else:
                ret['code'] = 1000
                ret['msg'] = "Login success!"
                token = LHKit.md5(user)
                playerinfo = LHKit.object_to_JSON(obj2)
                rt = {
                    'token':token,
                    'playerinfo':playerinfo,
                }
                ret['data'] = rt
                models.PlayerToken.objects.update_or_create(user=obj,defaults={'token':token})
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = 'Request abnormal! ' 

        return Response( ret ) 

class TeamListView(APIView): 
    authentication_classes = [Authtication]
    throttle_classes = [PSiteUserThrottle]
    #throttle_classes = [Visit2Throttle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            nowUser = models.PlayerInfo.objects.filter(player_login=request.user.id).first()
            teams  =  models.Team.objects.all().filter(league_belong=nowUser.player_league).order_by('-points','-goals_for')
            ret["data"] = LHKit.objects_to_JSON(teams)
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = 'Request abnormal! ' 
        return Response( ret )

from rest_framework import serializers
class PlayerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerInfo
        fields = "__all__"
        depth = 1 # 0~10 or 0~4 

class PlayerInfoView(APIView):
    authentication_classes = [Authtication]
    throttle_classes = [PSiteUserThrottle]
    #throttle_classes = [Visit2Throttle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            nowUser = models.PlayerInfo.objects.filter(player_login=request.user.id).first()
            jsNowUser = PlayerInfoSerializer(instance=nowUser,many = False)
            ret["data"] = jsNowUser.data 
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = 'Request abnormal! ' 
        return Response( ret )
