# Generated by Django 4.1.3 on 2024-08-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_level', models.IntegerField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seasoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('price_per_gram', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]