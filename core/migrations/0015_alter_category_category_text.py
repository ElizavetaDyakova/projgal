# Generated by Django 3.2.2 on 2021-06-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_text',
            field=models.CharField(max_length=100, verbose_name='Отделение'),
        ),
    ]
