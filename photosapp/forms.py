from django import forms
from .models import Photo, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user