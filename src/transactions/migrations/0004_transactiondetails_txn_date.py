# Generated by Django 2.2 on 2020-07-21 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20200720_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondetails',
            name='txn_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
