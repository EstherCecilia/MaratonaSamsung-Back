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
    id = models.IntegerField()
    name = models.CharField(max_length=100, primary_key=True)
    prevencao = models.ForeignKey(Prevencao, on_delete=models.CASCADE)
    sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sala(models.Model):
    name = models.CharField(max_length=60)
    publica = models.CharField(max_length=100)
    senha = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Sessao(models.Model):
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


