from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Set(models.Model):
    external_id = models.CharField(max_length=10, blank=False, null=False)
    input = models.CharField(max_length=200, blank=True, null=False)
    choice1 = models.CharField(max_length=200, blank=True, null=False)
    choice2 = models.CharField(max_length=200, blank=True, null=False)
    choice3 = models.CharField(max_length=200, blank=True, null=False)
    choice4 = models.CharField(max_length=200, blank=True, null=False)
    choice5 = models.CharField(max_length=200, blank=True, null=False)
    choice6 = models.CharField(max_length=200, blank=True, null=False)
    timestamp = models.DateTimeField()


class Choice(models.Model):
    choiceuser = models.ForeignKey(User)
    choiceset = models.ForeignKey(Set)
    choicemade = models.CharField(max_length=200, blank=False, null=False)
    timestamp = models.DateTimeField()

    def __str__(self):
        return "User : "+self.choiceuser.username+", Date and Time: "+self.timestamp.strftime('%m/%d/%Y')
