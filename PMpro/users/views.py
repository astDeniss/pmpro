from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Manager
from django.contrib.auth.models import User


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('projects-list')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            our_user = User.objects.get(username=username)
            company_name = form.cleaned_data.get('company_name')
            manager_profile = Manager(user=our_user, company_name=company_name)
            manager_profile.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration_page.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in :)")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is inactive.")
        else:

            return HttpResponse("Invalid login details given. Go back and try again")
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)

    return redirect('index')
