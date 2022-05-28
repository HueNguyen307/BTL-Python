from django.shortcuts import redirect
from User.models import User
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages

class LogoutUser(View):

	def get(self, request):
		logout(request)
		messages.success(request,"Logout successfully")
		return redirect('UserMember:login')




