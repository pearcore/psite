from django.contrib import admin
from .models import PlayerLogin,PlayerToken,League,Team,Role,PlayerInfo
# Register your models here.
admin.site.register(PlayerLogin)
admin.site.register(PlayerToken)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Role)
admin.site.register(PlayerInfo)



