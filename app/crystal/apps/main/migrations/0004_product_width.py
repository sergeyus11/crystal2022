# Generated by Django 4.0.5 on 2022-07-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_delete_сatalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(max_length=10, null=True, verbose_name='Вес'),
        ),
    ]
