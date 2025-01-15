from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class EmployeeSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Employee
        fields=['id','user','department','role']
        

class TaskSerializer(serializers.ModelSerializer):
    assigned_to=EmployeeSerializer()
    class Meta:
        model=Task
        fields=['id','title','descrption','assigned_to','status','created_at','due_date']

