# Generated by Django 3.1.5 on 2021-01-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzzvis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='articles',
            name='discription',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='customer',
            name='discription',
            field=models.CharField(max_length=9900),
        ),
    ]