# Generated by Django 2.2 on 2020-07-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('username', models.CharField(default=models.CharField(max_length=10), max_length=10)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('roll_no', models.CharField(max_length=10)),
                ('year_of_joining', models.IntegerField(default=2020, null=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin status')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'User Details',
                'verbose_name_plural': 'User Data',
            },
        ),
    ]
