from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
import logging

users = [
    {
        'course': 'МП-301',
        'last_name': 'Гражданко',
        'first_name': 'Кирилл',
        'middle_name': 'Генадьевич',
        'login': 'admin',
        'pass': 'password',
        'points': 10000182,
    },
    {
        'course': 'МП-302',
        'login': 'usr1',
        'pass': 'pass1',
		'last_name': 'Корчагина',
		'first_name': 'Екатерина',
		'middle_name': 'Сергеевна',
		'points': 506,
    },
    {
        'course': 'МН-302',
        'login': 'usr2',
        'pass': 'pass2',
		'last_name': 'Ефремова',
		'first_name': 'Елизавета',
		'middle_name': 'Владимировна',
		'points': 1026,
    },
    {
        'course': 'МП-302',
        'login': 'usr3',
        'pass': 'pass3',
		'last_name': 'Павлов',
		'first_name': 'Даниэль',
		'middle_name': 'Владимирович',
		'points': 102,
    },
]


def signin(request, login, password):
    for i in users:
        if i.get('login') == login:
            if i.get('pass') == password:
                request.session['Login'] = i.get('login')
                return True
    return False

# Create your views here.


def login(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    if authed(request):
        return redirect('/home/')
    else:
        return render(request, './Login/index.html')


def schedule(request):
    if authed(request):
        return render(request, './Schedule/index.html')
    return redirect('/login/')


def qr(request):
    if authed(request):
        return render(request, './QR/index.html')
    return redirect('/login/')


def home(request):
    if authed(request):
        return render(request, './Home/index.html')
    return redirect('/login/')


def authed(request):
    if request != None:
        if request.method == 'POST':
            if request.POST['action'] == "exit":
                request.session['Authed'] = False
                request.session['Login'] = ''
                return False
            if 'Authed' not in request.session:
                request.session.setdefault('Authed', False)
                request.session.setdefault('Login', '')
                if (signin(request, request.POST['login'], request.POST['password'])):
                    request.session['Authed'] = True
                    return True
            else:
                if request.session.get('Authed'):
                    return True
                else:
                    if (signin(request, request.POST['login'], request.POST['password'])):
                        request.session['Authed'] = True
                        return True
        else:
            if request.session.get('Authed'):
                return True
    request.session['Authed'] = False
    return False
