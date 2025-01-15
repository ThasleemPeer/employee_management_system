from django.db import models
from django.contrib.auth.models import User

#Department model

class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Employee Model

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)

    role=models.CharField(max_length=100,choices=[('admin','Admin'),('employee','Employee')],default='employee')

    def __str__(self):
        return self.user.username

#Task model
class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    assigned_to=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='tasks')
    created_At=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]

    status=models.CharField(max_length=200,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return f'{self.title} -{self.status}'
    
