from django.urls import path
from app.views import *


urlpatterns = [
    path('add/', AddAlarms.as_view()),
    path('get/all/', AddAlarms.as_view()),
    path('get/socket/', WebSocket.as_view()),
]
