from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(request):
    #return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
    return render(request, "hello/index.html")

def bob(request):
    return HttpResponse("Hello, Bob!")
    
def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    #return HttpResponse(f"Hello, {name}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })