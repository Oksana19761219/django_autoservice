# Generated by Django 4.0.4 on 2022-05-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice_1', '0002_remove_order_quantity_remove_order_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='image'),
        ),
    ]