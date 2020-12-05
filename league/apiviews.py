from rest_framework.views import APIView
from rest_framework.response import Response
from tools.LHStand import LHKit
from league import models

class LoginView(APIView): 
    authentication_classes = []
    #throttle_classes = [PSiteIPThrottle]
    #throttle_classes = [Visit2Throttle]
    def post(self, request , *args , **kwargs):
        ret = LHKit.LHResult()
        try:
            user = request.data["mobile"] #request._request.POST.get('username')
            password = request.data["password"] #request._request.POST.get('password')
            obj = models.PlayerLogin.objects.filter(mobile=user,password=password).first()
            if not obj:
                ret['code'] = 1001 
                ret['msg'] = "用户名或密码错误！"
            else:
                ret['code'] = 10000
                ret['msg'] = "登录成功"
                token = LHKit.md5(user)
                ret['data'] = token
                #有就更新，没有就创建
                models.PlayerToken.objects.update_or_create(user=obj,defaults={'token':token})
        except Exception as e:
            ret['code'] = 900
            ret['msg'] = '请求异常！' 

        return Response( ret ) 