# Generated by Django 3.2.10 on 2023-11-21 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_auto_20231122_0442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='pro_product_image1',
            new_name='pro_product_imagee',
        ),
        migrations.RenameField(
            model_name='productdb',
            old_name='pro_product_image2',
            new_name='pro_product_imageee',
        ),
    ]
