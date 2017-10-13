from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=30)

class Data(models.Model):
    datetime = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)