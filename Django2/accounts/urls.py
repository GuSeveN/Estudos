from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.Singup.as_view(), name='singup')
]
