# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 21:58:05 2014

@author: alex
"""
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')
=======
	url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
>>>>>>> 608791288c376b1b228d38d626f2f2f41c514e40
)
