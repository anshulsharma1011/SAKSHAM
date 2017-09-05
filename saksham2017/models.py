import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.


SPORTS_TYPE = (
    ('SOLO','SOLO'),
    ('TEAM','TEAM'),
    ('BOTH','BOTH')
)
TEAM_NAME_CHOICES = (
    ('Computer Science and Engineering','Computer Science and Engineering'),
    ('Information Technology','Information Technology'),
    ('Electronics and Communication Engineering','Electronics and Communication Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),
    ('Electricals Engineering','Electricals Engineering'),
    ('Electronics and Instrumentation','Electronics and Instrumentation'),
    ('MBA','MBA'),
    ('MCA','MCA'),
)
TEAM_INITIALS_CHOICES = (
    ('CSE','CSE'),
    ('IT','IT'),
    ('ECE','ECE'),
    ('ME','ME'),
    ('CE','CE'),
    ('EN','EN'),
    ('EI','EI'),
    ('MBA','MBA'),
    ('MCA','MCA'),
)
class AddSport(models.Model):
    sports_name = models.CharField(max_length=20,default='',unique=True)
    sports_type = models.CharField(max_length=5,default='',choices=SPORTS_TYPE)

    def __str__(self):
        return self.sports_name

    def get_absolute_url(self):
        return reverse('saksham2017:add_sports')

class AddTeams(models.Model):
    team_name = models.CharField(max_length=100,default='',unique=True,choices=TEAM_NAME_CHOICES)
    team_initials = models.CharField(max_length=3,default='',choices=TEAM_INITIALS_CHOICES)

    def __str__(self):
        return self.team_initials

    def get_absoulte_url(self):
        return reverse('saksham2017:add_teams')

class TrialsApplications(models.Model):
    class Meta:
        unique_together = (('user','sports_name'))

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    branch = models.CharField(max_length=100,default='')
    sports_name = models.ForeignKey(AddSport,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.branch

    def get_absolute_url(self):
        return reverse('saksham2017:index')

class Schedule(models.Model):
    host = models.CharField(max_length=100,default='')
    opponent = models.CharField(max_length=100,default='')
    pool = models.CharField(max_length=1,default='')
    match_no = models.IntegerField(default=0)
    date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    starting_date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    winner = models.CharField(max_length=100,default='')
    runner_up = models.CharField(max_length=100,default='')
    type = models.CharField(max_length=20,default='League')
    played = models.BooleanField(default=False)


    def __str__(self):
        return str(self.host + 'vs' +self.opponent )

    def get_abolute_url(self):
        return reverse('saksham2017:teams_details',kwargs={'pk':self.pk})
