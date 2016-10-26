# coding:utf-8
from django.conf.urls import patterns, include, url
from jcache.views import *

urlpatterns = patterns('',
                       url(r'^cache/cache_refresh/$', cache_refresh, name='cache_refresh'),
                       url(r'^cache/cache_setting/$', cache_setting, name='cache_setting'),
                       url(r'^cache/cache_urls/$', cache_urls, name='cache_urls'),

                      )