from django.shortcuts import render
from django.http import HttpResponse
from .service import *
from datetime import datetime

def index(request):
    context = {'title': 'Test'}
    return render(request, 'polygon/index.html', context=context)

def logs(request):
    logs_json = get_zabbix_logs()
    
    severity = {0: 'Not classified', 1: 'Information', 2: 'Warning', 3: 'Average', 4: 'High', 5: 'Disaster'} # severity of the event
    source = {0: 'Trigger', 1: 'Discovery rule', 2: 'Active agent autoregistration', 3: 'Internal event', 4: 'Service status update'} # type of the event

    logs = {i: (
        datetime.utcfromtimestamp(int(logs_json['result'][i]['clock'])).strftime('%Y-%m-%d %H:%M:%S'), 
        severity[int(logs_json['result'][i]['severity'])], 
        logs_json['result'][i]['name'],
        source[int(logs_json['result'][i]['source'])]
        ) for i in range(len(logs_json['result']))}

    return render(request, 'polygon/logs.html', {'logs': logs, 'title': 'Test'})

def network_topology(request):
    context = {'title': 'Test'}
    return render(request, 'polygon/network_topology.html', context=context)
