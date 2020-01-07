from django.contrib import admin
from django.urls import path,include

from django.urls import include, path #
from rest_framework import routers #

urlpatterns = [
    path('netask/', include('netask.urls')),
    path('admin/', admin.site.urls),
]
