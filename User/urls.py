from django import views
from django.contrib import admin
from django.urls import path
from User.view.login import LoginUser
from User.view.logout import LogoutUser
from User.view.register import Register
from User.view import views as account
app_name = "UserMember"
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('profile/', account.my_profile, name='profile'),
    path('profile-update/', account.profile_update, name='profile-update'),
    path('change-password/', account.change_password, name='change-password'),
]
