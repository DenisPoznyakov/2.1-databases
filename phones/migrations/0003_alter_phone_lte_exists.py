# Generated by Django 4.2.14 on 2024-08-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
    ]
