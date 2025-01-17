# Generated by Django 4.1.3 on 2024-08-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('stock_level', models.IntegerField(default=0)),
                ('wastage_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]
