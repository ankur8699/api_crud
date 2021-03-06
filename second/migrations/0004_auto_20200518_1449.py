# Generated by Django 3.0.6 on 2020-05-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0003_products_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('black', 'Black')], max_length=20)),
                ('image', models.ImageField(upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='color',
        ),
        migrations.RemoveField(
            model_name='products',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]
