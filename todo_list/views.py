from django.shortcuts import render, redirect
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

def delete(request, list_id):
    itemDelete = List.objects.get(pk = list_id)
    itemDelete.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('homepage')

def cross_off(request, list_id):
    itemCross = List.objects.get(pk = list_id)
    itemCross.completed = True
    itemCross.save()
    return redirect('homepage')

def uncross(request, list_id):
    itemUnCross = List.objects.get(pk = list_id)
    itemUnCross.completed = False
    itemUnCross.save()
    return redirect('homepage')