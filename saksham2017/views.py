from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .models import AddTeams,AddSport

# Create your views here.


class IndexView(TemplateView):
    template_name = 'saksham2017/index.html'


@method_decorator(user_passes_test(lambda u:u.is_superuser),name='dispatch')
class AddSportsView(CreateView):
    fields = ['sports_name','sports_type']
    model = AddSport
    template_name = 'saksham2017/add_sports.html'

@method_decorator(user_passes_test(lambda u:u.is_superuser),name='dispatch')
class AddTeamsView(CreateView):
    fields = ['team_initials','team_name']
    model = AddTeams
    template_name = 'saksham2017/add_sports.html'
