# Generated by Django 4.1.3 on 2024-08-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_inventorymovement_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorymovement',
            name='product',
        ),
    ]