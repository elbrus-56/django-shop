# Generated by Django 4.1.5 on 2023-01-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_products_image_alter_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/%Y-%m-%d/'),
        ),
    ]