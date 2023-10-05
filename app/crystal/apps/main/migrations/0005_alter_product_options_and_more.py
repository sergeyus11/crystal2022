# Generated by Django 4.0.5 on 2022-07-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_width'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='published',
            new_name='time_create',
        ),
        migrations.AddField(
            model_name='product',
            name='time_update',
            field=models.DateField(auto_now=True),
        ),
    ]