import json
from django.core import serializers
class LHKit:
    def objects_to_JSON(objects):
        #users = models.UserInfo.objects.filter(~Q(user_name=''))
        serializedModels = serializers.serialize("json", objects) 
        jsModels = json.loads(serializedModels)
        rtJson = []
        for temp in jsModels :
            one = temp['fields']
            one ['id'] = temp['pk']
            #one ['modelName'] = temp['model']
            rtJson.append (one)
        return rtJson
    def object_to_JSON(object):
        fakeArray = LHKit.objects_to_JSON([object])
        return fakeArray[0]

    def LHResult():
        rtModel = { # return model
        "code":1000,
        "msg":"ok2!",
        "data":0,
        }
        return rtModel