# Generated by Django 3.0.6 on 2020-05-18 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0004_auto_20200518_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='ids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_details', to='second.Products'),
        ),
    ]
