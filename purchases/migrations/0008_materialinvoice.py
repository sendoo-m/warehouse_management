# Generated by Django 4.1.3 on 2024-08-27 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0007_alter_purchaseinvoice_vat_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(default='Default Material', max_length=255)),
                ('material_unit', models.CharField(default='Unit Material', max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vat_material_purchase', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='purchases.vendors')),
            ],
        ),
    ]
