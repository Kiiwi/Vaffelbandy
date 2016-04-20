# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^takk/$', 'website.views.thanks', name='thanks'),
    url(r'^resultater/$', 'website.views.results', name='results'),

    url(r'^admin/', include(admin.site.urls)),
)