from pyzabbix.api import ZabbixAPI
import json
from datetime import datetime


def zabbix_auth(url='http://127.0.0.1/', user='Admin', password='zabbix'): # дефолтные значения - адрес zabbix веб интерфейяа, логин, пароль
    zapi = ZabbixAPI(url=url, user=user, password=password) # функция аутентификации
    return zapi
    

def get_zabbix_logs():
    zapi = zabbix_auth() # аутентификация
    logs_json = zapi.do_request('event.get', {'sortfield': ['clock'], "sortorder": "DESC"}) # выгрузка ивентов в формате json
    return logs_json

# Logout from Zabbix
# zapi.user.logout()