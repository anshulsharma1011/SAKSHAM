from django import forms
from .models import TrialsApplications,Schedule

class TrialsApplicationForm(forms.ModelForm):
    class Meta:
        model = TrialsApplications
        fields = ['sports_name']

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['starting_date']
