from django.contrib import admin
from .models import PlayerLogin,PlayerToken,League,Club
# Register your models here.
admin.site.register(PlayerLogin)
admin.site.register(PlayerToken)
admin.site.register(League)
admin.site.register(Club)


