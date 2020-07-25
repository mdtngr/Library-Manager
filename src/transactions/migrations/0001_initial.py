# Generated by Django 2.2 on 2020-07-20 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('fine_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('txn_id', models.IntegerField(primary_key=True, serialize=False)),
                ('txn_type', models.BooleanField(default=False)),
                ('fine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Fines')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
