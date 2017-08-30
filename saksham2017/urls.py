from django.conf.urls import url,include
from . import views
app_name = 'saksham2017'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^add_sports/$',views.AddSportsView.as_view(),name='add_sports'),
    url(r'^add_teams/$',views.AddTeamsView.as_view(),name='add_teams'),

]
