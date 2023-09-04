from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chat(request):
    return HttpResponse('')
def home(request):
    # response
    return render(request, 'home.html')

def single_chatroom(request):
    return render(request, "single_chatroom.html")

def group_chatroom(request):
    return render(request, "group_chatroom.html")

def deleted_chatroom(request):
    return render(request, "deleted_chatroom.html")


