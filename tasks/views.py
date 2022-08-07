from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar", "baz"]

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

#Add a new task
def add(request):
    return render(request, "tasks/add.html")