from django.conf.urls import url,include
from league import views

urlpatterns = [
    url(r'login/$' , views.LoginView.as_view()),
]