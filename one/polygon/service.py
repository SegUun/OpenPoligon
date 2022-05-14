from pyzabbix.api import ZabbixAPI
import json
from datetime import datetime


def zabbix_auth(url='http://127.0.0.1/', user='Admin', password='zabbix'):
    # Create ZabbixAPI class instance
    zapi = ZabbixAPI(url=url, user=user, password=password)
    return zapi
    

def get_zabbix_logs():
    zapi = zabbix_auth()
    logs_json = zapi.do_request('event.get')
    # logs_json = json.loads(result)
    return logs_json

# Logout from Zabbix
# zapi.user.logout()

logs_json = get_zabbix_logs()
logs = {}
for i in range(len(logs_json['result'])):
    name = logs_json['result'][i]['name']
    severity = logs_json['result'][i]['severity']
    time = datetime.utcfromtimestamp(int(logs_json['result'][i]['clock'])).strftime('%Y-%m-%d %H:%M:%S')
    logs[i] = name, severity, time

print(logs)


