from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, GENRE_CHOICES, CRITERIA_CHOICES

class ProfileCreationForm(UserCreationForm):
    favorite_genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False)
    preferred_criteria = forms.ChoiceField(choices=CRITERIA_CHOICES, required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                favorite_genre=self.cleaned_data.get('favorite_genre'),
                preferred_criteria=self.cleaned_data.get('preferred_criteria'),
                profile_picture=self.cleaned_data.get('profile_picture'),
            )
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'favorite_genre', 'preferred_criteria']
