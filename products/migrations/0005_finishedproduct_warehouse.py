# Generated by Django 4.1.3 on 2024-08-25 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_inventorymovement_raw_material_and_more'),
        ('products', '0004_finishedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishedproduct',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
    ]
