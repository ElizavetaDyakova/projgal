# Generated by Django 3.2.2 on 2021-06-16 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210616_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='spec',
            new_name='category',
        ),
    ]
