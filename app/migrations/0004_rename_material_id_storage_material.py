# Generated by Django 5.0.6 on 2024-06-14 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_material_id_productmaterial_material_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='material_id',
            new_name='material',
        ),
    ]