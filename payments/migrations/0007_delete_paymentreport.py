# Generated by Django 4.1.3 on 2024-08-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_paymentreport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentReport',
        ),
    ]
