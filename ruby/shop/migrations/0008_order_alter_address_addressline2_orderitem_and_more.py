# Generated by Django 4.2.3 on 2023-09-29 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_remove_product_stock_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'processing'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('refunded', 'refunded'), ('on_hold', 'on_hold')], default='pending', max_length=100)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='addressline2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_order')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
