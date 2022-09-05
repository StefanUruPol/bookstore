from django.shortcuts import render
from biblioteca.models import Libro
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from biblioteca.forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.


def index(request):
	return render(request, 'index.html')

def sobre(request):
	return render(request, 'sobre.html')

def buscar(request):
	if "busca" in request.GET and request.GET["busca"]:
		consulta = request.GET["busca"]
		libros = Libro.objects.filter(titulo__icontains=consulta)
		return render(request, 'resultados.html',{'libros':libros})
	else:
		return render(request, 'resultados.html')

def usuario_nuevo(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		try:
			formulario.save()
			return render(request, 'usuario_agregado.html')
		except:
			return render(request, 'usuario_no_agregado.html')
	else:
		formulario = UserCreationForm()
		return render(request, 'usuario_nuevo.html', {'formulario':formulario})

def contacto(request):
	if request.method =='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = "Correo desde la biblioteca"
			contenido = formulario.cleaned_data['mensaje'] + '\n\n'
			contenido += "Comunicarse al e-mail" + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['naranjo.valier@gmail.com'])
			try:
				correo.send()
				return render(request, 'correo_enviado.html')
			except:
				return render(request, 'correo_no_enviado.html')
	else:
		formulario = ContactoForm()
		return render(request, 'contacto.html', {'formulario':formulario}) 


def ingresar(request):
	if not request.user.is_anonymous:
		return HttpResponseRedirect('/privado')
	elif request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
			else:
				return render(request, 'no_usuario.html')
	else:
		formulario = AuthenticationForm()
		return render(request, 'ingresar.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render(request, 'privado.html',{'usuario': usuario})	


def salir(request):
	if not request.user.is_anonymous:
		logout(request)
		return HttpResponseRedirect('/ingresar')
	else:
		return render(request, 'no_logueado.html')


def error_404(request, exception):
	return render(request, '404.html', {})

def error_500(request):
	return render(request, '500.html', {})


