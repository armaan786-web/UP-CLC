# Generated by Django 4.0.2 on 2022-06-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_customuser_adhaar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='adhaar',
        ),
        migrations.AddField(
            model_name='customuser',
            name='adhaar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
