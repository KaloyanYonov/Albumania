from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import ProfileCreationForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            login(request, user)  # Automatically log in the user after registration
            return redirect('profile_dashboard')  # Redirect to their dashboard
    else:
        form = ProfileCreationForm()
    return render(request, 'Profile/register.html', {'form': form})



@login_required
def edit_profile(request):
    profile = request.user.profile  # Access the Profile model via the related user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile_dashboard')  # Redirect back to the profile dashboard
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def profile_dashboard(request):
    profile = request.user.profile
    return render(request, 'Profile/profile_dashboard.html', {'profile': profile})
