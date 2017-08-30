from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import TemplateView,View,CreateView,ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm

# Create your views here.

@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = 'accounts/index.html'

class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('accounts:profile-create')
        return render(request, self.template_name, {'form': form})

class ProfileCreate(CreateView):
    model = Profile
    fields = ['fullname', 'gender', 'branch', 'session', 'contact_details','accommodation','profile_photo']
    template_name = 'accounts/create_profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate,self).form_valid(form)
    success_url = reverse_lazy('accounts:index')


class AllUsersView(ListView):
    template_name = 'accounts/all_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Profile.objects.all().order_by('branch')


def CollegeCaptain(request):
    template_name = 'accounts/all_users.html'
    player = User.objects.get(pk = request.POST['player'])
    selected_player = Profile.objects.get(user = player)
    des = request.POST.get("design","")
    message  = "DATA ENTERED"
    if des == 'Remove':
        selected_player.designation = des
        selected_player.save()
        return HttpResponse(message)



    elif des == 'College Captain' or 'Branch Captain':
        selected_player.designation = des
        selected_player.save()
        return HttpResponse(message)

    elif (selected_player.designation == ('Branch Captain' or 'College Captain')) and des!='Remove':
        message = "Player already has a designation"
        return HttpResponse(message)
