from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import authenticate
from django.contrib.auth import login,logout
from .models import Task,Employee
from.serializers import TaskSerializer,EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework import status
class SignUpView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('passowrd')
        email = request.data.get('email')
        if User.objects.filter(username=username).exists():
            return Response({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return Response({'message':'user created successfully'},status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({'message':'loginsuccessful'})
        return Response({'error':'invalid credentials'})
class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return Response({'message':'logged out successfully'})
    
class TaskListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        employee=Employee.objects.all()
        if employee.role=='admin':
            tasks=Task.objects.all()
        else:
            tasks=Task.objects.filter(assigned_to=employee)

        serializer=TaskSerializer(tasks,many=True)

        return Response(serializer.data)
    


