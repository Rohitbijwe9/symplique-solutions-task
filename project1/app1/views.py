from django.shortcuts import render
from .models import Reminder
from . serializer import ReminderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def RemindView(request):
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)  # Pass request.data as the data argument
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        reminders = Reminder.objects.all()  # Assuming you have a Reminder model
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)