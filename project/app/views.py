from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, get_user, login
from .models import Products
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def main_render(request):
    return render(request, 'app/index.html', {'products': Products.objects.all()})

def show_product(request, sneak_id: int):
    product = get_object_or_404(Products, id=sneak_id)
    return render(request, 'app/product.html', {'product': product})

def show_profile(request, username: str):
	context = {}
	try:
		user = User.objects.get(username=username)

		context['username'] = user.username
		context['email'] = user.email

	except User.DoesNotExist:
		return HttpResponse("Something went wrong.")
	return render(request, 'app/profile.html', {'context': context})

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('main')
		else:
			messages.error(request, 'Ошибка авторизации или пользователь не обнаружен(')
	else:
		form = UserLoginForm()
	return render(request, 'app/login.html', {'form': form})

def user_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Поздравляю с регистрацией!')
			return redirect('main')
		else:
			messages.error(request, 'Регистрация не выполнена(')
	else:
		form = UserRegisterForm()
	return render(request, 'app/register.html', {'form': form})

def user_logout(request):
	logout(request)
	messages.success(request, 'Вы успешно вышли!')
	return redirect('main')