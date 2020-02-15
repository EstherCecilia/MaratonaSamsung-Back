from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings

from .models import *
from django.http import JsonResponse

# Create your views here.

def lista_doencas(request):
	# Primeiro, buscamos os termos
	doencas = list(Doenca.objects.values())

	# Incluímos no contexto
	contexto = {
		'doencas': doenca
	}

	# Retornamos o template no qual os termos serão dispostos
	return JsonResponse(contexto)
    
def lista_salas(request):
	# Primeiro, buscamos os termos
	salas = list(Sala.objects.values())

	# Incluímos no contexto
	contexto = {
		'salas': sala
	}

	# Retornamos o template no qual os termos serão dispostos
	return JsonResponse(contexto)
