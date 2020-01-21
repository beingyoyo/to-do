from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request, template_name="todo_list/home.html")

def about(request):
    return render(request, "todo_list/about.html")