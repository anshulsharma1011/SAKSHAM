import itertools
import datetime
import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView,ListView,View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import AddTeams,AddSport,TrialsApplications,Schedule
from accounts.models import Profile
from .forms import TrialsApplicationForm,ScheduleCreateForm


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

# @method_decorator(login_required,name='dispatch')
# class TrialsApplyView(CreateView):
#     fields = ['sports_name']
#     model = TrialsApplications
#     template_name = 'saksham2017/apply_trials.html'
#
#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super(TrialsApplyView,self).form_valid(form)
#     success_url = reverse_lazy('saksham2017:index')

@method_decorator(login_required,name='dispatch')
class TrialsApplyView(View):
    template_name = 'saksham2017/apply_trials.html'
    form_class = TrialsApplicationForm

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.branch = Profile.objects.get(user=request.user).branch
            app.save()
            return redirect('saksham2017:index')
        return render(request,self.template_name,{'form':form})



class ViewTrialsApplications(ListView):
    template_name = 'saksham2017/applications.html'
    context_object_name = 'application'

    def get_queryset(self):
        return TrialsApplications.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ViewTrialsApplications,self).get_context_data(**kwargs)
        usr = self.request.user
        br = Profile.objects.get(user = usr).branch
        context['apps'] = TrialsApplications.objects.filter(branch = br)
        return context

@method_decorator(user_passes_test(lambda u:u.is_staff),name='dispatch')
def SelectPlayers(request):
    for key in request.POST.keys():
        if 'app' in key:
            selected_user=TrialsApplications.objects.get(pk=int(key.replace('app',''))+4)
            selected_user.status = True
            selected_user.save()
    return HttpResponse("Players Selected")

class ScheduleCreateView(View):
    template_name = 'saksham2017/schedule_create.html'
    form_class = ScheduleCreateForm

    all_teams = []

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    for primary in range(1,len(AddTeams.objects.all())+1):
        initials = AddTeams.objects.get(pk=primary).team_initials
        all_teams.append(initials)

    if('EI' and 'CE') in all_teams:
        for n,i in enumerate(all_teams):
            if i == 'EI':
                all_teams[n] = 'CE + EI'

            elif i == 'MBA':
                all_teams[n] = 'MBA + MCA'

        del(all_teams[all_teams.index('CE')])
        del(all_teams[all_teams.index('MCA')])

    GP_A = all_teams[:int(len(all_teams)/2)]
    GP_B = all_teams[int(len(all_teams)/2)+1:]

    matches_GP_A = list(itertools.combinations(GP_A,2))
    matches_GP_B = list(itertools.combinations(GP_B,2))
    random.shuffle(matches_GP_A)
    random.shuffle(matches_GP_B)

    final = matches_GP_A

    for i in matches_GP_B:
        final.append(i)
    random.shuffle(final)

    def post(self,request):
        j = 0
        for i in self.final:
            j = j+1
            form = self.form_class(request.POST)
            sch = form.save(commit=False)
            sch.date = sch.starting_date + datetime.timedelta(days=j)
            sch.host = i[0]
            sch.opponent = i[1]
            if i[0] in self.GP_A:
                sch.pool = 'A'
            else:
                sch.pool = 'B'

            sch.starting_date = form.cleaned_data['starting_date']
            sch.match_no =  sch.match_no + j
            sch.save()
        return render(request,self.template_name,{'form':form})


class ScheduleView(ListView):
    template_name = 'saksham2017/schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
            return Schedule.objects.all().order_by('match_no')
