# Generated by Django 4.1.3 on 2024-08-23 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_finishedproduct'),
        ('inventory', '0008_inventorymovement_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymovement',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.finishedproduct'),
        ),
    ]