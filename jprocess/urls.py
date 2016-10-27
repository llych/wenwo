# coding:utf-8
from django.conf.urls import patterns, include, url
from jprocess.views import *

urlpatterns = patterns('',
                       url(r'^jprocess/jprocess_list/$', jprocess_list, name='jprocess_list'),
                       url(r'^jprocess/jprocess_list/(?P<server_id>.*)/(?P<group>.*)/(?P<app>.*)/stop/$', jprocess_stop, name='jprocess_stop'),
                       url(r'^jprocess/jprocess_list/(?P<server_id>.*)/(?P<group>.*)/(?P<app>.*)/start/$', jprocess_start, name='jprocess_start'),
                       url(r'^jprocess/jprocess_list/(?P<server_id>.*)/(?P<group>.*)/(?P<app>.*)/restart/$', jprocess_restart, name='jprocess_restart'),

                      )