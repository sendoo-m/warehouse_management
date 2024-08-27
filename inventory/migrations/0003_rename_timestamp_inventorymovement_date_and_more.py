# Generated by Django 4.1.3 on 2024-08-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventorymovement_warehouse_delete_inventory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventorymovement',
            old_name='timestamp',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='inventorymovement',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='inventorymovement',
            name='price',
        ),
        migrations.RemoveField(
            model_name='inventorymovement',
            name='wastage',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='description',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventorymovement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventorymovement',
            name='movement_type',
            field=models.CharField(choices=[('IN', 'In'), ('OUT', 'Out')], max_length=10),
        ),
    ]