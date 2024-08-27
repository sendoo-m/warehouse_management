# Generated by Django 4.1.3 on 2024-08-24 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_material_price_per_unit'),
        ('purchases', '0002_vendor_remove_purchaseorder_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='purchase_order',
        ),
        migrations.RemoveField(
            model_name='purchaseinvoice',
            name='purchase_order',
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='supplier',
            field=models.CharField(default='Unknown Supplier', max_length=100),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='invoice_date',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
        migrations.DeleteModel(
            name='PurchaseOrderItem',
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='purchases.purchaseinvoice'),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.material'),
        ),
    ]
