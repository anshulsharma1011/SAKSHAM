from django.contrib import admin
from .models import AddSport,AddTeams,TrialsApplications,Schedule
# Register your models here.

admin.site.register(AddSport)
admin.site.register(AddTeams)
admin.site.register(TrialsApplications)
admin.site.register(Schedule)
