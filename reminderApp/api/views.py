from django.shortcuts import render
from django.urls import path
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response


#import the created models
from .models import Notes, Reminders

#import the class from serializers.py
from .serializers import NoteSerializer, ReminderSerializer

#We add the CRUD here 
#create, update, delete 


#View all 
@api_view(['GET'])
def list_reminders(request):

    reminder = Reminders.objects.all()
    serializer = ReminderSerializer(reminder, many=True)

    return Response(serializer.data)


#View One
@api_view(['GET'])
def list_one(request, pk):

    reminder = Reminders.objects.get(id=pk)
    serializer = ReminderSerializer(reminder, many=False)
    
    return Response(serializer.data)


#post to api 
@api_view(['POST'])
def add_reminder(request):

    serializer = ReminderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#update to api 
@api_view(['POST'])
def update_reminder(request, pk):

    reminder = Reminders.objects.get(id=pk)
    serializer = ReminderSerializer(instance=reminder, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response("Reminder Updated")



#Delete a reminder 
@api_view(['DELETE'])
def delete_reminder(request, pk):

    reminder = Reminders.objects.get(id=pk)
    reminder.delete()

    return Response("Reminder Deleted")