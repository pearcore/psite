from django.urls import path

from . import views
app_name = 'finance'

urlpatterns = [
    path('typelist', views.typelist , name= 'typelist'),
    path('typeadd', views.typeadd , name= 'typeadd'),
    path('typedel', views.typedel , name= 'typedel'),
    path('recordlist', views.recordlist , name= 'recordlist'),
    path('recordadd', views.recordadd , name= 'recordadd'),
    path('recorddel', views.recorddel , name= 'recorddel'),
    path('recordclean', views.recordclean , name= 'recordclean'),
]