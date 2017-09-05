from django.conf.urls import url,include
from . import views
app_name = 'saksham2017'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^add_sports/$',views.AddSportsView.as_view(),name='add_sports'),
    url(r'^add_teams/$',views.AddTeamsView.as_view(),name='add_teams'),

    url(r'^apply/trials/$',views.TrialsApplyView.as_view(),name='trials_apply'),
    url(r'^apply/trials/select/$',views.SelectPlayers,name='select'),
    url(r'^view/trials/$',views.ViewTrialsApplications.as_view(),name='trials_applications'),

    url(r'^schedule/create/$',views.ScheduleCreateView.as_view(),name='schedule_create'),
    url(r'^schedule/view/$',views.ScheduleView.as_view(),name='schedule_list_view'),

]
