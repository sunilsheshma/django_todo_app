"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns =[
    path('list/<username>/',views.list_todo_items,name='list'),
    path('insert_todo/<username>/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<username>/<int:id>/',views.delete_todo_item,name='delete_todo_item'),
    path('complete_todo/<username>/<int:id>/', views.complete_todo_item, name='complete_todo_item'),
    path('delete_all/<username>/',views.delete_all,name='delete_all'),
    path('delete_completed/<username>/',views.delete_completed,name='delete_completed')
]
