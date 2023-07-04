from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),  
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('players/', views.PlayerList.as_view(), name="player_list"),
]