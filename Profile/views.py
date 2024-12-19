from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import ProfileCreationForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile

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
    logout(request)
    return redirect('home') 


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'Profile/login.html', {'form': form})


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
            return self.request.user.groups.filter(name="Staff").exists()

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class StaffOnlyView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Profile
    template_name = 'Profile/staff_view.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.filter(preferred_criteria='Melody')


class SuperuserOnlyView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = 'Profile/superuser_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_profiles'] = Profile.objects.count()
        return context