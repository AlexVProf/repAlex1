import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.models import ModelAlex


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def about(request):
    return render(request, 'about.html')


@csrf_exempt
def profile(request):
    if request.method == 'POST':
        response = redirect('/auth/')
        response.delete_cookie('isAuth')
        response.delete_cookie('name')
        return response
    try:
        if request.COOKIES['isAuth'] == 'true':
            return render(request, 'profile.html', {'login': 'Алексей'})
    except:
        pass
    return redirect('/reg/')


def page404(request, **kwargs):
    return render(request, 'page404.html', {'url': kwargs})


@csrf_exempt
def reg(request):
    if len(request.COOKIES.items()) > 0:
        return redirect('/profile/')
    if request.method == 'POST':
        login = request.POST.get('email')
        password = request.POST.get('password')
        user = ModelAlex()
        user.name = login
        user.password = password
        user.save()
        response = redirect('/profile/')
        response.set_cookie('isAuth', 'true')
        return response
    return render(request, 'register.html')


@csrf_exempt
def auth(request):
    if len(request.COOKIES.items()) > 0:
        return redirect('/profile/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = ModelAlex.objects.all()
        for i in data:
            if i.name == email and i.password == password:
                response = redirect('/profile/')
                response.set_cookie('isAuth', 'true')
                response.set_cookie('name', i.name)
                return response
        return render(request, 'auth.html', {'msg': 'Неверный логин или пароль'})
    return render(request, 'auth.html')
