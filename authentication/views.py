from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from chat.models import Room


class Login(View):

    def get(self, *args, **kwargs):
        return render(
            self.request,
            'login.html'
        )

    def post(self, args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/')
        else:
            messages.error(self.request, "Invalid credentials !")
            return redirect('/login/')


class SignUp(View):

    def get(self, *args, **kwargs):
        form = SignUpForm()

        return render(
            self.request,
            'signup.html',
            {
                "form" : form
            }
        )

    def post(self, *args, **kwargs):
        post = self.request.POST
        form = SignUpForm(post)
    
        if form.is_valid():
            form.save()
            user = authenticate(
                            username=post.get('username'), 
                            password=post.get('password1')
                        )
            if user is not None:
                login(self.request, user)

            return redirect("/")
        else:
            messages.error(self.request, "Inválid Infos")
            return redirect("/signup")


class LogOut(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('/')

    def post(self, *args, **kwargs):
        logout(self.request)
        return redirect('/')
