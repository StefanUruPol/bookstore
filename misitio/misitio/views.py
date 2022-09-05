from django.http import HttpResponse
from django.shortcuts import render
import datetime
import random
#En Django a las funciones se les llama vistas.

def hola(request):
	saludo = "Hola mundo!!!"
	return render(request, 'hola.html',{'saludo': saludo})

def fecha_actual(request):
	ahora = datetime.datetime.now()
	return render(request, 'fecha_actual.html', {'hora': ahora})

def aleatorio(request):
	numero = random.randint(1, 10)
	resto = numero % 2
	return render(request, 'aleatorio.html', {'numero': numero, 'resto': resto})

def semana(request):
	semana = [
		'lunes',
		'martes',
		'miércoles',
		'jueves',
		'viernes',
		'sábado',
		'domingo',
	]	
	return render(request, 'semana.html', {'semana': semana})


def horas_adelante(request, offset):
	diferencia = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=diferencia)
	return render(request, 'horas_adelante.html', {'dt':dt, 'diferencia': diferencia})

