from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        employees=Employee.objects.filter(employer__name=request.user.username)
        context={
            'employees':employees,
        }
        return render(request,'vacancy/hr.html',context)
    else:
        employers=Employer.objects.all()
        context={
            'employers':employers,
        }
        return render(request,'vacancy/Openings.html',context)


def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
         name = request.POST.get('username')
         pwd = request.POST.get('password')
         user = authenticate(request, username=name, password=pwd)
         if user is not None:
             login(request, user) 
             messages.info(request, f"You are now logged in as {name}")
             return redirect('home')
        return render(request, 'vacancy/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    Form = UserCreationForm
    if request.method == 'POST':
        Form = UserCreationForm(request.POST)
        if Form.is_valid():
            currUser = Form.save() 
            Employer.objects.create(user=currUser,name=currUser.username)
            return redirect('home') 
    context = {
        'form': Form,
    }
    return render(request, 'vacancy/register.html', context)


def apply(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('success')
    context = {
        'form': form,
    }
    return render(request, 'vacancy/apply.html', context)

def success(request):
    return render(request, 'vacancy/success.html')