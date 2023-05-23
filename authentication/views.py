from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            print("user")
            login(request, user)
            return redirect('/')
        else:
            print("not")
            messages.error(request, "Invalid credentials !")
            return redirect('/login/')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')