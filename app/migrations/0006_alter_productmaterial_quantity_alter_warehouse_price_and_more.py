# Generated by Django 5.0.6 on 2024-06-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_storage_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaterial',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='remainder',
            field=models.FloatField(),
        ),
    ]
