# Generated by Django 4.0.5 on 2022-07-06 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_categorys_alter_product_time_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categorys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categorys'),
        ),
    ]
