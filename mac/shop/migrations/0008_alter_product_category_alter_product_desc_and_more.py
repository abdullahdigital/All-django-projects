# Generated by Django 5.0.6 on 2024-06-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=150),
        ),
    ]
