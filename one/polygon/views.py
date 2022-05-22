from django.shortcuts import render
from django.http import HttpResponse
from .service import *
from datetime import datetime
from django.http import HttpResponse


def index(request):
    return render(request, 'polygon/index.html', {'title': 'OpenPolygon'})

def logs(request):
    logs_json = get_zabbix_logs() # аутентификация

    severity = {0: 'Not classified', 1: 'Information', 2: 'Warning', 3: 'Average', 4: 'High', 5: 'Disaster'} # важноть события
    source = {0: 'Trigger', 1: 'Discovery rule', 2: 'Active agent autoregistration', 3: 'Internal event', 4: 'Service status update'} # тип события
    object = {0: 'Trigger', 1: 'Discovered host', 2: 'Discovered service', 3: 'Auto-registered host', 4: 'Item', 5: 'LLD rule', 6: 'Service'} # тип объекта, к которому относится событие
    value = {0: 'OK', 1: 'Problem', 2: 'host or service discovered', 3: 'host or service lost'} # состояние связанного объекта

    '''
    генератор словаря где ключ - индекс + 1 (так как индекс идет с 0 а нам он понадобится для нумерации ивентов в таблице на сайте, мы же не будем нумеровать с 0)
    значение - информация выгружаемая в поле таблицы из json документа, полученного из zabbix api
    '''
    logs = {i+1: (
        datetime.utcfromtimestamp(int(logs_json['result'][i]['clock'])).strftime('%Y-%m-%d %H:%M:%S'),
        severity[int(logs_json['result'][i]['severity'])], 
        logs_json['result'][i]['name'],
        source[int(logs_json['result'][i]['source'])],
        object[int(logs_json['result'][i]['object'])],
        value[int(logs_json['result'][i]['value'])]
        ) for i in range(len(logs_json['result']))}

    return render(request, 'polygon/logs.html', {'logs': logs, 'title': 'Events'})

def network_topology(request):
    return render(request, 'polygon/network_topology.html', {'title': 'Network Topology'})
