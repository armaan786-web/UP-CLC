# Generated by Django 4.0.2 on 2022-06-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_member_adhaar_customuser_adhaar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_img', models.ImageField(upload_to='course_pic')),
                ('course_name', models.CharField(max_length=100)),
                ('course_amt', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('course_location', models.CharField(max_length=100)),
            ],
        ),
    ]
