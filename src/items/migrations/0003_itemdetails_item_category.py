# Generated by Django 2.2 on 2020-07-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200721_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='item_category',
            field=models.CharField(default='None', max_length=15),
        ),
    ]