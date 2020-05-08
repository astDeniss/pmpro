from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Manager
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user_profile = User(username=username, password=password, first_name=first_name, last_name=last_name)
            
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

