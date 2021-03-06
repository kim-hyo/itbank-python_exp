"""mainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from phonebook import views

app_name = 'PB'

urlpatterns = [
    path(r'', views.pbook, name='pb'),
    path(r'test/', views.test),
    path(r'testint/<int:ids>', views.testint),
    path(r'detail/<int:userid>', views.details, name='detail'),
    path(r'modify/<int:userid>', views.modify, name='mod'),        
    path(r'delete/<int:userid>', views.delete, name='del'),   
    path(r'add/', views.add, name='add'),      
]

