from django.urls import *
from .views import LoginView,LogoutView,TaskListView,SignUpView

urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view,name='logout'),
    path('tasks/',TaskListView.as_view(),name='task-list'),
    path('signup/',SignUpView.as_view(),name='signup'),

]
