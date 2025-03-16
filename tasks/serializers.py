from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'assigned_to': {'read_only': True}}  # Prevent user from providing 'assigned_to'
