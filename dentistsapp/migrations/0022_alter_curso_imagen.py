# Generated by Django 4.2.4 on 2023-11-23 19:53

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsapp', '0021_alter_curso_enlace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=(1140, 1521), upload_to='cursos', verbose_name='Imagen'),
        ),
    ]
