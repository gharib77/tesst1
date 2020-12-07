# Generated by Django 3.1.3 on 2020-12-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20201202_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('qte', models.IntegerField()),
                ('date_entr', models.DateTimeField()),
            ],
            options={
                'db_table': 'produits',
            },
        ),
    ]