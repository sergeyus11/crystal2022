# Generated by Django 4.0.5 on 2023-08-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_categorys_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_product',
            field=models.BooleanField(default=False, verbose_name='новинка'),
        ),
    ]
