from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import Profile
from .formss import UserRegistrationForm, ProfileUpdateForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Profile')
        else:
            return render(request, 'Profile/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Profile/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'Profile/register.html', {'form': form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'Profile/profile.html', {'form': form})
