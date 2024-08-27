# Generated by Django 4.1.3 on 2024-08-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_finishedproduct'),
        ('inventory', '0003_rename_timestamp_inventorymovement_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='location',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inventorymovement',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='inventorymovement',
            name='movement_type',
            field=models.CharField(choices=[('IN', 'إضافة'), ('OUT', 'خصم')], max_length=3),
        ),
        migrations.AlterField(
            model_name='inventorymovement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.finishedproduct'),
        ),
    ]