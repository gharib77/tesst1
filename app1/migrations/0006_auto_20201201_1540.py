# Generated by Django 3.1.3 on 2020-12-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20201201_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecrivain',
            name='age',
            field=models.CharField(max_length=40),
        ),
    ]
