from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from.models import Todo
from django.contrib.auth.models import User,auth
# Create your views here.

def list_todo_items(request, username):
    todo_list = Todo.objects.filter(name=username)
    return render(request, 'todo_list.html', {'todo_list': todo_list})

def insert_todo_item(request,username):
    content = request.POST['content']
    todo = Todo(name=username,content=content)
    todo.save()
    string ='/todo/list/'+username
    return redirect(string)

def delete_todo_item(request,username,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    string = '/todo/list/' + username
    return redirect(string)

def complete_todo_item(request,username,id):
    todo=Todo.objects.get(id=id)
    todo.complete=True
    todo.save()
    string = '/todo/list/' + username
    return redirect(string)

def delete_all(request,username):
    todo=Todo.objects.filter(name=username)
    todo.delete()
    string = '/todo/list/' + username
    return redirect(string)

def delete_completed(request,username):
    todo=Todo.objects.filter(name=username,complete=True)
    todo.delete()
    string = '/todo/list/' + username
    return redirect(string)
