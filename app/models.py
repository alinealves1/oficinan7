from django.db import models

# Create your models here.

class Cliente(models.Model):
    Nome = models.CharField(max_length=120)
    Data_Nasc = models.DateField()
    CPF = models.CharField(max_length=13)
    RG = models.CharField(max_length=10)
    Telefone = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
