from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm


def index(request):

    form = TaskForm() #tyhjä lomake luodaan
    tasks = Task.objects.all() #hakee tehtävät tietokannasta

    if request.method == 'POST':
        form = TaskForm(request.POST) #täyttää lomakkeen lähetetyllä datalla
        if form.is_valid(): #tarkistaa onko annettu data oikeassa muodossa
            form.save()

        return redirect('/') #ohjataan pääsivulle

    context = {'tasks': tasks, 'TaskForm': form} 
    return render(request, 'tasks.html', context) 


def updateTask(request, pk):
    #olemassa olevan tehtävän päivitys
    task = Task.objects.get(id=pk) 
    form = TaskForm(instance=task) 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'TaskForm': form}
    return render(request, 'update-task.html', context)


def deleteTask(request, pk):
    #poistaa tehtävän tietokannasta
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task': task}
    return render(request, 'delete-task.html', context)

def toggleComplete(request, pk):
    #vaihtaa tehtävän tilan
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/')
