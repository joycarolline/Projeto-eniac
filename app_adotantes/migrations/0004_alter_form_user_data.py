# Generated by Django 4.2.11 on 2024-04-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adotantes', '0003_alter_form_user_options_form_user_animal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_user',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
    ]