# Generated by Django 3.2.2 on 2021-06-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210616_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='god_grad',
            field=models.DateField(blank=True, null=True, verbose_name='Год выпуска'),
        ),
    ]