from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect 

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
				return False;
			if 'Authed' not in request.session:
				request.session.setdefault('Authed', False)
				if (request.POST['login'] in ["DarkUFO", "LaxyLax", "Arteom", "Darya",]):
					if (request.POST['password'] == 'admin'):
						request.session['Authed'] = True
						return True
			else:
				if request.session.get('Authed', True):
					return True
				else:
					if (request.POST['login'] in ["DarkUFO", "LaxyLax", "Arteom", "Darya",]):
						if (request.POST['password'] == 'admin'):
							request.session['Authed'] = True
							return True
		else:
			if request.session.get('Authed', True):
				return True
	request.session['Authed'] = False
	return False