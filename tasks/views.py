from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Task
from . forms import TaskForm, RegisterForm


def register_view(request):
    #rekisteröinti
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Rekisteröinti onnistui!')
            return redirect('/')
        else:
            messages.error(request, 'Rekisteröinti epäonnistui. Tarkista tiedot.')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    #kirjautuminen
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Tervetuloa takaisin, {username}!')
            return redirect('/')
        else:
            messages.error(request, 'Virheellinen käyttäjätunnus tai salasana')
    
    return render(request, 'login.html')


def logout_view(request):
    #uloskirjautuminen
    logout(request)
    messages.success(request, 'Olet kirjautunut ulos')
    return redirect('login')


@login_required(login_url='login')
def index(request):

    form = TaskForm() #tyhjä lomake luodaan
    tasks = Task.objects.filter(user=request.user) #hakee vain kirjautuneen käyttäjän tehtävät

    if request.method == 'POST':
        form = TaskForm(request.POST) #täyttää lomakkeen lähetetyllä datalla
        if form.is_valid(): #tarkistaa onko annettu data oikeassa muodossa
            task = form.save(commit=False)
            task.user = request.user #asettaa käyttäjän
            task.save()
            messages.success(request, 'Tehtävä luotu!')

        return redirect('/') #ohjataan pääsivulle

    context = {'tasks': tasks, 'TaskForm': form} 
    return render(request, 'tasks.html', context) 


@login_required(login_url='login')
def updateTask(request, pk):
    #olemassa olevan tehtävän päivitys
    task = Task.objects.get(id=pk, user=request.user) 
    form = TaskForm(instance=task) 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tehtävä päivitetty!')
            return redirect('/')
        
    context = {'TaskForm': form}
    return render(request, 'update-task.html', context)


@login_required(login_url='login')
def deleteTask(request, pk):
    #poistaa tehtävän tietokannasta
    task = Task.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tehtävä poistettu!')
        return redirect('/')
    
    context = {'task': task}
    return render(request, 'delete-task.html', context)


@login_required(login_url='login')
def toggleComplete(request, pk):
    #vaihtaa tehtävän tilan
    task = Task.objects.get(id=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('/')
