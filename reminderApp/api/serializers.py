from rest_framework import serializers
from .models import Notes, Reminders

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminders
        fields = '__all__'




class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'



