# Generated by Django 4.0.5 on 2022-08-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_cafe_retailer_name_adress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_v',
            options={'ordering': ['time_create', 'name'], 'verbose_name': 'Название продукта', 'verbose_name_plural': 'Названия продуктов'},
        ),
        migrations.AlterField(
            model_name='product_v',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Название продукта'),
        ),
    ]
