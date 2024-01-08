from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, profile_view, edit_profile_view, change_password_view

urlpatterns = [
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('profile', profile_view, name='profile_view'),
    path('edit_profile', edit_profile_view, name='edit_profile_view'),
    path('change_password', change_password_view, name='change_password_view'),
]
