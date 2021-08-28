from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import SignUpForm,postview
from django.views.generic import ListView,DeleteView
# Create your views here.

def home(request):
    return render(request, 'home.html')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm
    return render(request, 'registration/register.html',{'form':form})

class postview(ListView):
    '''if request.method == "POST":
        posting = request.POST.get('posting')
        postin = postview(posting=posting)
        postin.save()
    return render(request, 'registration/login.html')'''
    model = postview
    template_name = 'posting.html'