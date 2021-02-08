from django.shortcuts import render
from django.http import JsonResponse

#Adding REST framework imports 
from rest_framework.decorators import api_view
from rest_framework.response import Response


#import serializer
from .serializers import TaskSerializer 


#GET/ POST Method usin gg decorators 
@api_view(['GET', 'POST'])
def apiOverview(request):

    api_urls = {
        "List" : '/task-list/'
    }

    return Response(api_urls)


#import thr moddels (task) to render view 
from .models import Task

@api_view(['GET'])
def task_list(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


#Way to add data  / creat -> POST
@api_view(['POST'])
def task_create(request):

    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
