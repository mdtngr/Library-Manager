# Generated by Django 3.0.6 on 2020-08-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_itemdetails_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='static_cdn/img'),
        ),
    ]
