from rest_framework.permissions import BasePermission

class SVIPPermission(BasePermission):
    message = '必须是SVIP才能访问!'
    def has_permission(self,request,view):
        rtAllow = False
        if request.user.user_type == 3 :
            return True
        return rtAllow

class NormalPermission(BasePermission):
    message = '必须是普通用户,或者VIP用户才能访问!'
    def has_permission(self,request,view):
        rtAllow = False
        if ((request.user.user_type == 1) or (request.user.user_type == 2))  :
            return True
        return rtAllow