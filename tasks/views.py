from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):

    form = TaskForm()
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks.html', context)


def updateTask(request, pk):

    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'TaskForm': form}
    return render(request, 'update-task.html', context)


def deleteTask(request, pk):

    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'delete-task.html', context)


def toggleComplete(request, pk):

    task = get_object_or_404(Task, id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/')
