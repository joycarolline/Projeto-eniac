# Generated by Django 4.2.11 on 2024-04-11 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adotantes', '0005_alter_form_user_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form_user',
            old_name='email',
            new_name='email_adotante',
        ),
        migrations.RenameField(
            model_name='form_user',
            old_name='info_geral',
            new_name='info_geral_adotante',
        ),
        migrations.RenameField(
            model_name='form_user',
            old_name='nome',
            new_name='nome_adotante',
        ),
        migrations.RenameField(
            model_name='form_user',
            old_name='telefone',
            new_name='telefone_adotante',
        ),
    ]
