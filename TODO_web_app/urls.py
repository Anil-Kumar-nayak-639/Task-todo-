from django.contrib import admin
from django.urls import path,include
from TODO_web_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>',views.delete_task,name='delete_task'),
    path('completed/<id>',views.completed,name='completed'),
    path('pending/<id>',views.pending,name='pending'),
]
