from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            allListItems = List.objects.all
            messages.success(request, ('Item has been added to list!'))
            return render(request, "todo_list/home.html", {'all_items': allListItems})
    else:
        allListItems = List.objects.all
        return render(request, "todo_list/home.html", {'all_items':allListItems})

def about(request):
    return render(request, "todo_list/about.html")