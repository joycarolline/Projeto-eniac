# Generated by Django 4.2.11 on 2024-04-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_voluntarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
