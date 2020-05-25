# Generated by Django 3.0.6 on 2020-05-25 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_clothe_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clothe',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='clothes',
            new_name='products',
        ),
    ]
