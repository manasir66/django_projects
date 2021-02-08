from rest_framework import serializers
from .models import Task

#create a class you want to render json 

class TaskSerializer(serializers.ModelSerializer):

    #Use the meta class to define the model and which filds to display 
    class Meta:

        model = Task
        fields = '__all__' #all fields

