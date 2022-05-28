from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages

class LoginUser(View):

	def post(self, request):
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = name, password = password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.error(request,'Login failed: username or password is incorrect')
			return redirect('UserMember:login')
	def get(self, request):
		return render(request, 'queenok/login.html')

	
