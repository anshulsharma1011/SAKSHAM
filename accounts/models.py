from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
GenderChoices=(
    ('Male','Male'),
    ('Female','Female'),
)

BranchChoices = (
    ('CSE','Computer Science and Engineering'),
    ('IT','Information Technology'),
    ('ECE','Electronics and Communication Engineering'),
    ('ME','Mechanical Engineering'),
    ('CE','Civil Engineering'),
    ('EN','Electricals Engineering'),
    ('EI','Electronics and Instrumentation'),
    ('MBA','MBA'),
    ('MCA','MCA'),
)
AccommodationChoices=(
    ('Hosteler','Hosteler'),
    ('Day Scholar','Day Scholar'),
)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=GenderChoices, default='')
    branch = models.CharField(max_length=250, choices=BranchChoices, default='CSE')
    session = models.CharField(max_length=20, default='')
    contact_details = models.CharField(max_length=15, default='')
    accommodation = models.CharField(max_length=20, choices=AccommodationChoices, default='')
    designation = models.CharField(max_length=20,default='')
    profile_photo = models.FileField(null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.pk})
