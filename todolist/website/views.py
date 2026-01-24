from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import transaction
from django.db.models import Max
from django.contrib import messages
from .models import Task
from .forms import AddTaskForm

def home(request):
    tasks = Task.objects.all().order_by("view_order")
    return render(request, "home.html", {"tasks": tasks})


def reorder_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    action = request.POST.get("action")

    if action == "up":
        neighbor = (
            Task.objects
            .filter(view_order__lt=task.view_order)
            .order_by("-view_order")
            .first()
        )

    elif action == "down":
        neighbor = (
            Task.objects
            .filter(view_order__gt=task.view_order)
            .order_by("view_order")
            .first()
        )

    else:
        return redirect('home')

    if neighbor:
        # swap orders
        task.view_order, neighbor.view_order = (
            neighbor.view_order,
            task.view_order,
        )

        task.save()
        neighbor.save()

    return redirect('home')


def add_task(request):
    form = AddTaskForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            # Get the next order number
            order_last = (
                Task.objects.aggregate(Max("view_order"))["view_order__max"] or 0
            )
            
            # Save the form and set the order
            task = form.save(commit=False)
            task.view_order = order_last + 1
            task.save()
            
            messages.success(request, "Tarefa adicionada com sucesso!")
            return redirect('home')
    
    return render(request, "add_task.html", {'form': form})
  

def delete_task(request, pk):
    delete_task = Task.objects.get(id=pk)
    delete_task.delete()
    messages.success(request, "Task Deleted Successfully...")
    return redirect('home')


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if request.method == "POST":
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa editada com sucesso!")
            return redirect('home')
        else:
            # If form has errors, still return to home (error handling in modal)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('home')
    
    return redirect('home')