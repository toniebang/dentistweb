# Generated by Django 4.2.4 on 2023-11-23 07:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsapp', '0011_alter_curso_lecciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='lecciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5000, null=True), size=8), size=8),
        ),
    ]
