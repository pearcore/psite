from rest_framework.throttling import SimpleRateThrottle,BaseThrottle

class Visit3Throttle (SimpleRateThrottle):
    scope = "LuffyUser"

    def get_cache_key(self,request,view):
        return request.user.username

class Visit2Throttle (SimpleRateThrottle):
    scope = "Luffy"

    def get_cache_key(self,request,view):
        return self.get_ident(request)

import time
VISIT_RECORD = {}
class VisitTrottle(BaseThrottle):
    def __init__(self):
        self.history = None

    def allow_request(self, request , view):
        remote_addr = request.META.get('REMOTE_ADDR')
        ctime = time.time()

        if remote_addr not in VISIT_RECORD :
            VISIT_RECORD [remote_addr] = [ctime,]
            return True
        history = VISIT_RECORD.get(remote_addr)
        self.history = history
        while history and history[-1] <  ctime - 60 :
            history.pop()
        if len(history) < 3:
            history.insert(0,ctime)
            return True
        

        #return True
    def wait(self):
        ctime = time.time()
        
        return 60 - (ctime - self.history[-1])