from django.db import models
from django.core.urlresolvers import reverse

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
    sports_name = models.CharField(max_length=20,default='',primary_key=True)
    sports_type = models.CharField(max_length=5,default='',choices=SPORTS_TYPE)

    def __str__(self):
        return self.sports_name

    def get_absolute_url(self):
        return reverse('saksham2017:add_sports')

class AddTeams(models.Model):
    team_name = models.CharField(max_length=100,default='',primary_key=True,choices=TEAM_NAME_CHOICES)
    team_initials = models.CharField(max_length=3,default='',choices=TEAM_INITIALS_CHOICES)

    def __str__(self):
        return self.team_initials

    def get_absoulte_url(self):
        return reverse('saksham2017:add_teams')
