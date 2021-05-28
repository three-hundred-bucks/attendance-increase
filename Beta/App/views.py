from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect 
import logging

users = [
{
	'login': 'LaxyLax',
	'pass': 'helpme',
	'name': 'Олеся Денисовна Панченко',
	'points': 10000182,
},
{
	'login': 'DarkUFO',
	'pass': 'admin',
	'name': 'Андрей Сергеевич Михалев',
	'points': 506,
},
{
	'login': 'Darya',
	'pass': 'IDarya',
	'name': 'Дарья Владимировна Мелехина',
	'points': 1026,
},
{
	'login': 'Art',
	'pass': '007',
	'name': 'Артем Владимирович Петрушенко',
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
				return False;
			if 'Authed' not in request.session:
				request.session.setdefault('Authed', False)
				request.session.setdefault('Login', '')
				if (signin(request, request.POST['login'], request.POST['password'])):
					request.session['Authed'] = True
					return True
			else:
				if request.session.get('Authed', True):
					return True
				else:
					if (signin(request, request.POST['login'], request.POST['password'])):
						request.session['Authed'] = True
						return True
		else:
			if request.session.get('Authed', True):
				return True
	request.session['Authed'] = False
	return False