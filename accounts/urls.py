from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$',auth_views.login,{'template_name':'accounts/login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'/accounts/login/'},name='logout'),
    url(r'^profile/new/$', views.ProfileCreate.as_view(), name='profile-create'),
    url(r'^all_users/$', views.AllUsersView.as_view(), name='all_users_list'),
    url(r'^all_users/college_captain',views.CollegeCaptain,name='college_captain'),

]
