from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="tasks"),

    path('update-task/<str:pk>/', views.updateTask, name="update-task"),

    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),

    path('toggle-complete/<str:pk>/', views.toggleComplete, name='toggle-complete'),

]