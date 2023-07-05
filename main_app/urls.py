from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),  
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('players/', views.PlayerList.as_view(), name="player_list"),
    path('teams/new/', views.TeamCreate.as_view(), name='team_create'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team_detail'),
    path('teams/<int:pk>/update', views.TeamUpdate.as_view(), name='team_update'),
    path('teams/<int:pk>/delete', views.TeamDelete.as_view(), name="team_delete"),
]