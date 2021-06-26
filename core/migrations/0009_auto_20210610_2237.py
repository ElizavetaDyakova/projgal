# Generated by Django 3.2.2 on 2021-06-10 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_fio_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='otdel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otdel', to='core.otdel'),
        ),
        migrations.AlterField(
            model_name='card',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='core.specialnost'),
        ),
    ]