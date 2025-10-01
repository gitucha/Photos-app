from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signup/', views.signup, name='signup'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('photo_upload/', views.upload_photo, name='photo_upload'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
      ]