# Generated by Django 4.2.4 on 2023-11-23 07:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsapp', '0010_curso_lecciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='lecciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5000), size=8), size=8),
        ),
    ]
