# Generated by Django 3.1.5 on 2021-01-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzzvis', '0002_auto_20210128_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='discription',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_paragraph',
            field=models.TextField(max_length=1000),
        ),
    ]
