from django.shortcuts import render
from .forms import  EmailAuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import Permission, User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_exist = User.objects.filter(email=request.POST.get('email', None))
        if not user_exist:
            if form.is_valid():
                form.save()

    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())

    return render(request, 'signin.html', {'form': form})
