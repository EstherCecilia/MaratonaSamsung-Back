from django.conf import settings
from django.db import models


# Create your models here.
class Sintoma(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Prevencao(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Doenca(models.Model):
    ident = models.IntegerField()
    name = models.CharField(max_length=100, primary_key=True)
    prevencoes = models.ManyToManyField(Prevencao)
    sintomas = models.ManyToManyField(Sintoma)

    def __str__(self):
        return self.name


class Sala(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    publica = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sessao(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    doencas = models.ManyToManyField(Doenca)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


