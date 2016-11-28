# coding:utf-8
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from jumpserver.api import *
from jperm.perm_api import user_have_perm
from django.http import HttpResponseNotFound




def purl_url(url):
    try:
        status_code = requests.request('PURGE',url,headers={'iask':'abc123'},timeout=10).status_code
        if status_code in [200,404] :
            return True
    except Exception, e:
        return False

@require_role('admin')
def jdeploy(request):
    """ 发布管理 """

    path1 , path2 ='发现管理','项目上线'
    return my_render('jdeploy/jdeploy.html',locals(),request)



