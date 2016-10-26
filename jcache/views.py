# coding:utf-8
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from jumpserver.api import *
from jperm.perm_api import user_have_perm
from django.http import HttpResponseNotFound

from jumpserver.settings import LOG_DIR
import zipfile
import json
import pyte
import requests
# logger.debug("ffffffff")


def purl_url(url):
    try:
        status_code = requests.request('PURGE',url,headers={'iask':'abc123'},timeout=10).status_code
        if status_code in [200,404] :
            return True
    except Exception, e:
        return False

@require_role('admin')
def cache_refresh(request):
    """ 刷新缓存 """
    # return HttpResponseNotFound(u'没有此进程!')
    path1 , path2 ='缓存管理','刷新缓存'
    return my_render('jcache/cache_refresh.html',locals(),request)

@require_role('admin')
def cache_setting(request):
    """ 缓存设置 """

    return my_render('jcache/cache_refresh.html', locals(), request)

@require_role('admin')
def cache_urls(request):
    """ 获取URLS """
    urls = request.POST.get('urls',"").splitlines()
    success = 0
    fail = 0

    for url in urls:
        # print url
        if purl_url(url):
            success +=1
        else:
            fail += 1

    return HttpResponse(json.dumps({'success':success,'fail':fail}))
    # return my_render('jcache/cache_refresh.html', locals(), request)

@require_role('admin')
def log_detail(request):
    return my_render('jcache/cache_refresh.html', locals(), request)
