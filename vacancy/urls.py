from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('apply/', views.apply, name='apply'),
    path('success/', views.success, name='success'),
]