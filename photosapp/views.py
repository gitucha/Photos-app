from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Profile
from .forms import PhotoForm, ProfileForm, SignUpForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('index')    

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {'form': form})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo_detail.html', {'photo': photo})

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    return redirect('photo_detail', pk=pk)