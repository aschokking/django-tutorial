# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 21:58:05 2014

@author: alex
"""
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))
