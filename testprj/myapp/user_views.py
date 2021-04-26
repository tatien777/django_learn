from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login 


import time

def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save_user()
            return redirect('list_students')
        else: 
            for errors in form.errors:
                print(errors)
    return render(
        request=request,
        template_name="user/register.html",
        context={
            'form':form
        },
        )
def login_user(request):
    form = LoginForm()
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user: 
                print("Login successed ")
                message = "login successed"
                login(request,user)
                time.sleep(3)
                return redirect('list_students')
            else: 
                print("Login failed ")
                message = "failed try again "
        else: 
            for errors in form.errors:
                print(errors)
        
    return render(
        request=request,
        template_name="registration/login.html",
        context={
            'form':form,
            'message':message,
        },
        )