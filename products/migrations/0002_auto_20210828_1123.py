# Generated by Django 3.2.5 on 2021-08-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productview',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productview',
            name='weight',
            field=models.CharField(max_length=50),
        ),
    ]
