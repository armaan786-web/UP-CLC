# Generated by Django 4.0.2 on 2022-10-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_role_active_role_inactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]