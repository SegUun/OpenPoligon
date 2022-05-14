from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('logs/', logs, name='logs'),
    path('network_topology/', network_topology, name='network_topology'),
]