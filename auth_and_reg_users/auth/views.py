from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    template = 'signup.html'

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data['username'], form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            return redirect(home)

    context = {'form': form}

    return render(
        request,
        template,
        context
    )
