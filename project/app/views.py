from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, get_user, login
from .models import Products, Cart
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Cart

# Create your views here.

def main_render(request):
    return render(request, 'app/index.html', {'products': Products.objects.all()})

def settings_render(request):
	return render(request, 'app/')

def show_product(request, sneak_id: int):
<<<<<<< HEAD
	product = get_object_or_404(Products, id=sneak_id)
	cart_item = Cart.objects.filter(user=request.user, product=product)
	has_items = bool(cart_item)
	if request.method == 'POST':
		if 'add_product' in request.POST:
			cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

			if not created:
				cart_item.quanity += 1
				cart_item.save()
				return redirect('main')
			
		elif 'remove_product' in request.POST:
			cart_item = Cart.objects.get(user=request.user, product=product)
			cart_item.delete()


	return render(request, 'app/product.html', {'product': product, 'has_items': has_items})
=======
    product = get_object_or_404(Products, id=sneak_id)
    cart_items = Cart.objects.filter(user=request.user,product=product)
    has_items = bool(cart_items)
    if request.method == 'POST':
        if 'add_product' in request.POST:
            cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
            
            if not created:
                cart_item.quanity += 1
                cart_item.save()
                return redirect('/')
            
        elif 'remove_tovar' in request.POST:
            cart_item = Cart.objects.get(user=request.user, product=product)
            cart_item.delete()
        
    return render(request, 'app/product.html', {'product': product,'has_items':has_items})
>>>>>>> 22fde60a6e69883344a0e6115f03b0ccac886a50


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