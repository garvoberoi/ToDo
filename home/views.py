from django.shortcuts import render, redirect
from .forms import Toform, signupform
from home.models import ToDo
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def home(request):
    form = Toform()
    contents = ToDo.objects.all().order_by("-date")
    return render(request, 'index.html', {'contents':contents, 'form':form})

@login_required(login_url='signin')
def add_content(request):
    if request.method == 'POST':
        form = Toform(request.POST)
        if form.is_valid():
            form.save()
            
        form = Toform() 
    return HttpResponseRedirect("/")
    
@login_required(login_url='signin')   
def delete_content(request, content_id):
    ToDo.objects.get(id=content_id).delete()
    return HttpResponseRedirect("/")

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = signupform()
        if request.method =='POST':
            form = signupform(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, 'Your account was created for '+ user)
                return redirect('signin')
        return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect !!')
                return render(request, 'signin.html')
        return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

    
    