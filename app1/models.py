from django.db import models

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
    class Meta:
        db_table='personnes'
    def __str__(self):
        return self.nom

