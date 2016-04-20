# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from .forms import RegistrationForm
from .models import Team, TournamentStatus
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    form = RegistrationForm(request.POST or None)
    current_teams = Team.objects.values
    tournament_status = TournamentStatus.objects.values
    if form.is_valid():

        # Save form
        save_it = form.save(commit=False)
        save_it.save()


        # Get form data
        team_name = form.cleaned_data["team_name"]
        team_from = form.cleaned_data["team_from"]
        tournament_class = form.cleaned_data["tournament_class"]
        phone = form.cleaned_data["phone"]
        email = form.cleaned_data["email"]
        other = form.cleaned_data["other"]
        #messages.success(request, "success message")  # Django message

        # Email information
        email_recipient = ["tommy.lee.ryan@gmail.com"]
        email_subject = "[Frederikscup] %s" % team_name
        email_body = "Lagnavn: %s" \
                     "\nFra: %s" \
                     "\nKlasse: %s" \
                     "\nTelefon: %s" \
                     "\nE-post: %s" \
                     "\nAnnet: %s" % (team_name, team_from, tournament_class,
                                      phone, email, other)
        send_mail(email_subject, email_body, 'tommy.lee.ryan@gmail.com',
                  email_recipient, fail_silently=False)

        return HttpResponseRedirect("takk")

    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))


def thanks(request):
    tournament_status = TournamentStatus.objects.values
    return render_to_response("takk.html", locals(),
                              context_instance=RequestContext(request))


def results(request):
    tournament_status = TournamentStatus.objects.values
    return render_to_response("resultater.html", locals(),
                              context_instance=RequestContext(request))


def custom_404(request):
    return render(request, "404.html", {}, status=404)


def custom_500(request):
    return render(request, "500.html", {}, status=500)