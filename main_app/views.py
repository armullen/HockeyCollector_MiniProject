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
    Player("Patrice Burgeron", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk86pT9NWI4QP27AkjV814ngGI52dUHCB74A&usqp=CAU", "Center", "St. Patrice", "2003-present", "Canadian" ),
    Player("Cam Neely", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM9SfGvl9GCHIsWK4CVuvp5yM-Rc0j9jJhzQ&usqp=CAU", "Right Wing", "Bam-Bam-Cam", "1983-1996", "Canadian"),
    # ---------------------Blackhawks-------------------------------
    Player("Bobby Hull", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxxggPfQpOGg30o5EKf7_kPre3dltIwSFlcQ&usqp=CAU", "Winger", "The Golden Jet", "1957-1980", "Canadian"),
    Player("Patrick Kane", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd1Ld78ImJPMVXbmJwFHrYWV1SYYy-9MJQZw&usqp=CAU", "Right Wing", "Showtime", "2007-present", "American"),
    Player("Chris Chelios", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHhdV_pdiPPl1sTtZtcZ_fjovZyT_0HHv_XA&usqp=CAU", "Defenseman", "Soft Hands Chelios", "1984-2010", "American"),
    Player("Stan Mikita", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRszDNY2x0luqd2PRLY9a62NLZS4QPojsRqgA&usqp=CAU", "Center", "Stosh", "1958-1980", "Slovakian/Canadian"),
    # -------------------------Rangers---------------------------
    Player("Brian Leetch", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNPGMoDdywNCeweoMcG2ufG8kPY1Mt22F7fw&usqp=CAU", "Defenseman", "None", "1987-2006", "American"),
    Player("Mark Messier", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSqp0rOc1C0iodEsQiv7mkIISROvQZJ6CR6w&usqp=CAU", "Center", "Moose", "1979-2004", "Canadian"),
    Player("Mike Richter", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6JDMQq-fHcU5wyC0DRdVcP5uOgoVIE0gIBw&usqp=CAU", "Goalie", "None", "1989-2003", "American"),
    Player("Henrik Lundqvist", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk7rkyeKfbBibKQ44lX5ziISCqEqG3-ajrnQ&usqp=CAU", "Goalie", "Ricky", "1997-2018", "Sweedish"),
    # ------------------------Maple Leafs----------------------------
    Player("Mats Sundin", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR40YK9E7dsniyglgXWg2ITkUZ6pSy6tqn2A&usqp=CAU", "Center", "Weed", "1989-2009", "Sweedish"),
    Player("Doug Gilmore", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTT8NGtPbZFGftp5HX1uzcduJhINzDLw5eIbA&usqp=CAU", "Center", "Killer", "1983-2003", "Canadian"),
    Player("Wendel Clark", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeXEEpg3KjU2LT5fy-TONNMBRvAb4APR5bHQ&usqp=CAU", "Left Wing", "Capitan Crunch", "1985-2000", "Canadian"),
    Player("Auston Matthews", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1B6_XzFVEo5mtYrMDFsSax1LRdfhfAhBHMw&usqp=CAU", "Center", "Papi", "2015-present", "American"),
    # --------------------------Canadians----------------------------
    Player("Guy Laffleur", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4p6eZNaEuyaxFm9heq701x5q5FCXu_wIgVQ&usqp=CAU", "Right Wing", "The Flower", "1971-1991", "Canadian"),
    Player("Maurice Richard", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgSQYxQcs30SLYn3xQ9OideLUVBJXPyntkPA&usqp=CAU", "Right Wing", "Rocket", "1948-1951", "Canadian"),
    Player("Patrick Roy", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWvk-aAAX4eGgCubnQhah03fkZP0MSbxitlQ&usqp=CAU", "Goalie", "Saint Patrick", "1984-2003", "Canadian"),
    Player("Saku Koivu", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf7woOx_CXGlY_48wuJo5EOoxKH-wSg0e4bw&usqp=CAU", "Center", "Capitan K","1992-2014", "Finish"),

]