from pyzabbix.api import ZabbixAPI
import json
from datetime import datetime


def zabbix_auth(url='http://127.0.0.1/', user='Admin', password='zabbix'):
    zapi = ZabbixAPI(url=url, user=user, password=password)
    return zapi
    

def get_zabbix_logs():
    zapi = zabbix_auth()
    logs_json = zapi.do_request('event.get', {'sortfield': ['clock'], "sortorder": "DESC"})
    return logs_json

# Logout from Zabbix
# zapi.user.logout()

logs_json = get_zabbix_logs()