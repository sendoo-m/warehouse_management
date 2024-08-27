# Generated by Django 4.1.3 on 2024-08-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('PM', 'Project Manager'), ('WM', 'Warehouse Manager'), ('SS', 'Salesperson'), ('PS', 'Purchaseperson')], max_length=2),
        ),
    ]
