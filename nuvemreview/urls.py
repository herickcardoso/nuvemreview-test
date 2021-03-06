# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from cadastro.views import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'cadastro.views',
    url(r'^$', 'home', name='home'),
    url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
    url(r'^lista/$', Listar.as_view(), name='lista'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^barras/','barras', name='barras'),
    url(r'^radar/','radar', name='radar'),
    url(r'^review/','review', name='review'),
    url(r'^table/','table', name='table'),
)
