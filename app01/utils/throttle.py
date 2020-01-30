from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
import time
Vist_Record = {

}

class LHThrottle(BaseThrottle):
    def __init__(self):
        self.history = None

    def allow_request(self,request, view):
        rtAllow = False
        remote_addr = request._request.META.get('REMOTE_ADDR')
        ctime = time.time()
        if remote_addr not in Vist_Record :
            Vist_Record[remote_addr] = [ctime,]
            rtAllow = True
        else :
            history = Vist_Record.get(remote_addr)
            self.history = history
            while history and history[-1] < (ctime - 10) :
                history.pop()
            if len(history) >= 3 :
                rtAllow = False
            else :
                history.insert(0,ctime)
                rtAllow = True
        return rtAllow
    def wait(self):
        rt = 10 
        ctime = time.time()
        rt = 10 - ( ctime - self.history[-1] )
        return rt


class PSiteIPThrottle(SimpleRateThrottle):
    scope = "PSiteIPThrottleRate"
    def get_cache_key(self,request,view):
        return self.get_ident(request)

class PSiteUserThrottle(SimpleRateThrottle):
    scope = "PSiteUserThrottleRate"
    def get_cache_key(self,request,view):
        return request.user.user_name
