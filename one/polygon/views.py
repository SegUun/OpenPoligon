from django.shortcuts import render
from django.http import HttpResponse
from .service import *
from datetime import datetime

def index(request):
    context = {'title': 'Test'}
    return render(request, 'polygon/index.html', context=context)

def logs(request):
    logs_json = get_zabbix_logs()
    logs = {}
    for i in range(len(logs_json['result'])):
        name = logs_json['result'][i]['name']
        severity = logs_json['result'][i]['severity']
        time = datetime.utcfromtimestamp(int(logs_json['result'][i]['clock'])).strftime('%Y-%m-%d %H:%M:%S')
        logs[i] = time, severity, name

    return render(request, 'polygon/logs.html', {'logs': logs, 'title': 'Test'})

def network_topology(request):
    context = {'title': 'Test'}
    return render(request, 'polygon/network_topology.html', context=context)
