# Generated by Django 4.0.2 on 2022-06-29 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_job_job_des_job_job_experience_job_job_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='employee',
        ),
    ]
