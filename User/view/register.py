from django.shortcuts import render, redirect
from User.models import User
from django.views import View
from django.contrib import messages

class Register(View):
	def get(self, request):
		return render(request, 'queenok/login.html')

	def post(self, request):
		name = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password']
		password2 = request.POST['confirm-password']
		try:
			User.objects.get(username = name)
		except:
			if password1 == password2:
				user = User.objects.create_user(username = name, email = email, password = password1)
				user.save()
				messages.success(request,'Register successfully. Please login here')
				return redirect('UserMember:login')
			else:
				messages.error(request, 'Passwords do not match')
				return redirect('UserMember:login')
		messages.error(request, 'This username has been taken')
		return redirect('UserMember:login')			



		