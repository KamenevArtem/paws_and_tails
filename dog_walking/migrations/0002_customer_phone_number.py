# Generated by Django 4.0.10 on 2023-11-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_walking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=40, verbose_name='Номер телефона'),
        ),
    ]