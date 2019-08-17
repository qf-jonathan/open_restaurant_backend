from django.urls import path
from core import consumers

websocket_urlpatterns = [
    path('ws/ambient/', consumers.AttendanceConsumer),
    path('ws/kitchen/', consumers.AttendanceConsumer),
]
