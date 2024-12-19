from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import ProfileCreationForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            login(request, user)  
            return redirect('profile_dashboard')  
    else:
        form = ProfileCreationForm()
    return render(request, 'Profile/register.html', {'form': form})



@login_required
def edit_profile(request):
    profile = request.user.profile  
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile_dashboard')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'Profile/edit_profile.html', {'form': form})


@login_required
def profile_dashboard(request):
    profile = request.user.profile
    return render(request, 'Profile/profile_dashboard.html', {'profile': profile})



def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirects to the home page


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'Profile/login.html', {'form': form})