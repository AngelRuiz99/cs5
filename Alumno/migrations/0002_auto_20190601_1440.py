# Generated by Django 2.2.1 on 2019-06-01 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='ap_mat',
            new_name='apellidoMaterno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='ap_pat',
            new_name='apellidoPaterno',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='profesorAsig',
            new_name='id_profesor',
        ),
    ]
