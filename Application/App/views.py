from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect 
import logging

users = [
{
	'course': 'МП-302',
	'last_name': 'Панченко',
	'first_name': 'Олеся',
	'middle_name': 'Денисовна',
	'login': 'LaxyLax',
	'pass': 'helpme',
	'points': 10000182,
},
{
	'course': 'МП-301',
	'login': 'DarkUFO',
	'pass': 'admin',
	'last_name': 'Михалев',
	'first_name': 'Андрей',
	'middle_name': 'Сергеевич',
	'points': 506,
},
{
	'course': 'МН-302',
	'login': 'Darya',
	'pass': 'IDarya',
	'last_name': 'Мелехина',
	'first_name': 'Дарья',
	'middle_name': 'Владимировна',
	'points': 1026,
},
{
	'course': 'МП-302',
	'login': 'Art',
	'pass': '007',
	'last_name': 'Петрушенко',
	'first_name': 'Артем',
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
				return False;
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