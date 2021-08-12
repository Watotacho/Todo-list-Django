from django import urls
from django.urls import path
from .views import  register_Task

urlpatterns = [
    path("register/",register_Task,name="listTask"),
]