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

class Player(TemplateView):
    def __init__(self, name, img, position, nickname, years, nationality):
        self.name = name
        self.image = img
        self.position = position
        self.nickname = nickname
        self.years = years
        self.nationality = nationality

players = [
    # -------------------Red Wings_______________________
    Player("Pavel Datsyuk", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSx6yw0gZRbebVvlrazcdpFEDxv98m6TaAmg&usqp=CAU", "Center", "The Magic Man", "1996-2021", "Russian"),
    Player("Gordie Howe", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKCiuXm4Ib3gYGBuZR8sYHkcb-CDNLZ_n63Q&usqp=CAU", "Right Wing", "Mr. Hockey", "1946-1980", "Canadian"),
    Player("Steve Yzerman", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQURSf3EuIUllOSOaJx4VRNjUkxWecOmp0JGg&usqp=CAU", "Center", "Stevie Y", "1983-2006", "Canadian"),
    Player("Nick Lindstrom",  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSruuEHv0dC2dag6Zsn1c96Ra-LAVmi1jgfw&usqp=CAU", "Defensmen", "The Perfect Human", "1998-2012", "Sweedish"),
    # --------------------Bruins---------------------------
    Player("Bobby Orr", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYNpZCEAfeDwLacYI1qYwln9d_FYrX_3pZZQ&usqp=CAU","Defensmen", "Number 4", "1966-1978", "Canadian"),
    Player("Ray Bourque", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2tqGug9x1jXdLEksrnPqVyKhvAnlfobjPyQ&usqp=CAU", "Defensmen" "None", "1979-2001", "Canadian"),
    Player("Patrice Burgeron")
    Player("Cam Neely")
    # ---------------------Blackhawks-------------------------------
    Player("Bobby Hull")
    Player("Patrick Kane")
    Player("Chris Chelios")
    Player("Stan Mikita")
    # -------------------------Rangers---------------------------
    Player("Brian Leetch")
    Player("Mark Messier")
    Player("Mike Richter")
    Player("Henrik Lundqvist")
    # ------------------------Maple Leafs----------------------------
    Player("Mats Sundin")
    Player("Doug Gilmore")
    Player("Wendel Clark")
    Player("Auston Matthews")
    # --------------------------Canadians----------------------------
    Player("Guy Laffleur")
    Player("Maurice Richard")
    Player("Patrick Roy")
    Player("Daly Koivu")

]