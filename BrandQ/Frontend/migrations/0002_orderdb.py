# Generated by Django 4.2.11 on 2024-05-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('First_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Apartment', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Postal_Zip', models.CharField(blank=True, max_length=100, null=True)),
                ('Email_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Product', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
