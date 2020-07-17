from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Clock
from app.serializers import ClockSerializer
from datetime import datetime
import socket


class AddAlarms(APIView):
    """Adding an alarm"""

    def post(self, request):
        """Method of adding an alarm clock"""
        data = request.data.get('data')
        serializer = ClockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get(self, request):
        """Receiving data"""
        alarms = Clock.objects.filter(time__gte=datetime.now())
        serializer = ClockSerializer(alarms, many=True)
        return Response({"data": serializer.data})


class WebSocket(APIView):
    """Websocket"""

    def get(self, request):
        pass
        # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # server_socket.bind(('127.0.0.1', 8000))
        # server_socket.listen()
        # while True:
        #     print('Connection')
        #     client_socket, addr = server_socket.accept()
        #     # print('Connection from', addr)
        #     while True:
        #         alarms = Clock.objects.get(time=datetime.now())
        #         serializer = ClockSerializer(alarms, many=True)
        #           if alarms:
        #               return Response({"data": serializer})

