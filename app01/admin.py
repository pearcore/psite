from django.contrib import admin

# Register your models here.
from .models import UserInfo,UserToken

# admin.site.register(Question)
admin.site.register(UserInfo)
admin.site.register(UserToken)