from rest_framework.throttling import SimpleRateThrottle,BaseThrottle

class PSiteIPThrottle(SimpleRateThrottle):
    scope = "PSiteIPThrottleRate"
    def get_cache_key(self,request,view):
        return self.get_ident(request)

class PSiteUserThrottle(SimpleRateThrottle):
    scope = "PSiteUserThrottleRate"
    def get_cache_key(self,request,view):
        return request.user.mobile