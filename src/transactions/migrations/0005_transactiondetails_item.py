# Generated by Django 2.2 on 2020-07-22 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200721_0510'),
        ('transactions', '0004_transactiondetails_txn_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondetails',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.ItemDetails'),
            preserve_default=False,
        ),
    ]
