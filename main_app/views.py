from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Team, Player
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'

class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['teams'] = Team.objects.filter(name__icontains=name)
            context['header'] = f'Serching for {name}'
        else:
            context['teams'] = Team.objects.all()
            context['header'] = 'Original Six Teams'
        return context
    
class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'img', 'arena']
    template_name = 'team_create.html'
    success_url = "/team"

class TeamDetail(DetailView):
    model = Team
    template_name = 'team_detail.html'

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'img', 'arena']
    template_name = 'team_update.html'
    
    def get_success_url(self):
        return reverse('team_detail', kwargs={'pk': self.object.pk})
    
class TeamDelete(DeleteView):
    model = Team
    template_name = 'team_delete_confirmation.html'
    success_url= '/teams/'

class PlayerList(TemplateView):
    model = Player
    template_name = 'player_list.html'

class PlayerCreate(View):

    def post(self, request, pk):
        name= request.POST.get('name')
        image= request.POST.get('img')
        position= request.POST.get('position')
        nickname= request.POST.get('nickname')
        nationality= request.POST.get('nationality')
        Player.objects.create(name=name, image=image, position=position, nickname=nickname, nationality=nationality)
        return redirect('player_detail' pk=pk)
