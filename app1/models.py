from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Grade(models.Model):
    libelle =models.CharField(max_length=80)

    class Meta:
        db_table='grades'
    def __str__(self):
        return self.libelle

class Personne(models.Model):
    nom=models.CharField(max_length=60)
    prenom=models.CharField(max_length=60)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    date_nais=models.DateField(auto_now_add=False,auto_now=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table='personnes'
    def __str__(self):
        return self.nom


class Ecrivain(models.Model):
    name=models.CharField(max_length=40)
    age=models.CharField(max_length=40)
    class Meta:
        db_table='ecrivains'
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)
    ecrivain=models.ForeignKey(Ecrivain,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name

