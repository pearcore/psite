class LHPermission(object):
    def has_permission(self,request,view):
        rtAllow = False
        if request.user.user_type == 3 :
            return True
        return rtAllow