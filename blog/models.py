from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=100)
    author= models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        db_table='articles'
    def __str__(self):
        return self.title

