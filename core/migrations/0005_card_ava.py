# Generated by Django 3.2.2 on 2021-05-18 18:40

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_otdel_name_specialnost_otdel'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='ava',
            field=models.ImageField(default=None, upload_to=core.models.add_path),
        ),
    ]
