from django.conf.urls import url,include
from league import apiviews

urlpatterns = [
    url(r'login/$' , apiviews.LoginView.as_view()),
    url(r'teamlist/$' , apiviews.TeamListView.as_view()),
    url(r'playerinfo/$' , apiviews.PlayerInfoView.as_view()),
    url(r'matcheslist/$' , apiviews.MatchesListView.as_view()),
]