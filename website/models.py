# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
# Create your models here.
CLASS_CHOICES = (
    ('H', 'Herrer'),
    ('D', 'Damer'),
    ('A', 'Åpen'),
)


class Registration(models.Model):
    team_name = models.CharField(max_length=100, blank=False)
    team_from = models.CharField(max_length=100, blank=False)
    tournament_class = models.CharField(max_length=100,
                                        choices=CLASS_CHOICES, blank=False,
                                        default="Herrer")
    email = models.CharField(blank=False, max_length=100)
    phone = models.CharField(max_length=15, blank=False)
    other = models.TextField(max_length=256, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.tournament_class + ' ' + self.team_name


class Team(models.Model):
    team_name = models.CharField(max_length=100, blank=False)
    team_from = models.CharField(max_length=100, blank=False)
    tournament_class = models.CharField(max_length=100,
                                        choices=CLASS_CHOICES, blank=False,
                                        default="Herrer")
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.tournament_class + ' ' + self.team_name


class TournamentStatus(models.Model):
    signup = models.BooleanField(default=True)
    pre_start = models.BooleanField()
    started = models.BooleanField()

    class Meta:
        verbose_name = "Tournament Status"
        verbose_name_plural = "Tournament Status"

    def __unicode__(self):
        return "Status"
