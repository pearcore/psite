from django.conf.urls import url,include
from league import apiviews

urlpatterns = [
    url(r'login/$' , apiviews.LoginView.as_view()),
    url(r'clublist/$' , apiviews.ClubListView.as_view()),
]