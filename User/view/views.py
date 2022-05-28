from django.shortcuts import redirect, render
from django.http import HttpResponse
from User.models import User
from User.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
def my_profile(request):
    current_user = request.user
    profile = User.objects.get(username= current_user.username)
    context = {'profile': profile}
    return render(request, 'queenok/profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('UserMember:profile')
    else:
        profile_form = ProfileForm(instance=request.user)
        context = {
            'profile_form': profile_form,
        }
        return render(request, 'queenok/profile_update.html', context)
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('UserMember:profile')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('UserMember:change-password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'queenok/update_password.html', {'form': form})