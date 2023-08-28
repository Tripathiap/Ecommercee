from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm



def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('store')
        
        else:
            messages.success(request,("There was an error logging in!"))
            return redirect('login')
        
    else:
        return render(request, 'members/login.html',{})


def logout_view(request):
    logout(request)
    return redirect('store')


def register_user(request):
    if request.method == "POST":
        form = UserForm()  
        if form.is_valid():  
            form.save()
        return redirect('login')
    else:  
        form = UserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'members/register.html', context) 
