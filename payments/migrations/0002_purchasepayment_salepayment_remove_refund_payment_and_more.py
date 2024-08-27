# Generated by Django 4.1.3 on 2024-08-26 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('purchases', '0007_alter_purchaseinvoice_vat_percentage'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('BANK_TRANSFER', 'Bank Transfer'), ('CASH', 'Cash on Delivery')], max_length=20)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='SalePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('BANK_TRANSFER', 'Bank Transfer'), ('CASH', 'Cash on Delivery')], max_length=20)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='refund',
            name='payment',
        ),
        migrations.AddField(
            model_name='refund',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='reason',
            field=models.CharField(choices=[('RETURNED_GOODS', 'Returned Goods'), ('CANCELLED_ORDER', 'Cancelled Order'), ('OTHER', 'Other')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='refund',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.purchasepayment'),
        ),
    ]