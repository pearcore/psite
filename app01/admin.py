from django.contrib import admin
from .models import UserInfo,UserToken,UserRole,UserGroup

admin.site.register(UserInfo)
admin.site.register(UserToken)

admin.site.register(UserRole)
admin.site.register(UserGroup)
