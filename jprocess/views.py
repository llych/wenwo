# coding:utf-8
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from jumpserver.api import *
from jperm.perm_api import user_have_perm
from django.http import HttpResponseNotFound

from supervisor_manage import get_status, get_server_id_mapping, get_group_mapping, batch_group_opt, batch_server_opt

group_mapping = get_group_mapping()
server_id_mapping = get_server_id_mapping()
def purl_url(url):
    try:
        status_code = requests.request('PURGE',url,headers={'iask':'abc123'},timeout=10).status_code
        if status_code in [200,404] :
            return True
    except Exception, e:
        return False

@require_role('admin')
def jprocess_list(request):
    """ 进程管理 """
    apps=get_status(group_mapping)
    path1 , path2 ='进程管理','supervisor管理'
    return my_render('jprocess/jprocess.html',locals(),request)

@require_role('admin')
def jprocess_stop(request,server_id, group, app):
    """ 进程管理  stop"""
    app_name = '%s:%s' % (group, app)
    # print server_id
    # print '----'
    # print server_id_mapping
    # print server_id_mapping.get(server_id)
    return HttpResponse(server_id_mapping.get(server_id).stop_process(app_name))



@require_role('admin')
def jprocess_start(request,server_id, group, app):
    """ 进程管理  start"""
    app_name = '%s:%s' % (group, app)
    return HttpResponse(server_id_mapping.get(server_id).start_process(app_name))

@require_role('admin')
def jprocess_restart(request,server_id, group, app):
    """ 进程管理  restart"""
    app_name = '%s:%s' % (group, app)
    return HttpResponse(server_id_mapping.get(server_id).restart_process(app_name))


