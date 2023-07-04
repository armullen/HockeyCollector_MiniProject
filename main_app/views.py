from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'

class Team:
    def __init__(self, name, img, arena):
        self.name = name
        self.image = img
        self.arena = arena

teams = [
    Team("Detroit Red Wings", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVzGMcRrmFisco1UiuytnirM9GTbQU6qeCTA&usqp=CAU", "Little Caesars Arena"),
    Team("Chicago Blackhawks", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1AgPtuT-iiLYOBkf2erBulbsPZZxoSeCIOg&usqp=CAU", "United Center"),
    Team("Montreal Canadians","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4Hq2tl3g97ubAzqHqpZjEctmZLgQ1xuqDNw&usqp=CAU", "Bell Centre"),
    Team("Boston Bruins", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIhusVVzhurMevIZDGmR-HH_GXZPMeNDjVEQ&usqp=CAU", "TD Garden"),
    Team("New York Rangers", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSv4hxUxnomtF9xliffOKZzhvihdQEUHE9AvA&usqp=CAU", "Madison Square Garden"),
    Team("Toronto Maple Leafs", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXSgv5D6AwTV3AdNPR1kYfRI_OrbcwUovpCA&usqp=CAU", "Scotiabank Arena")
]

class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = teams
        return context
