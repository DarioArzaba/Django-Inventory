# Generated by Django 4.2.4 on 2023-08-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_added',)},
        ),
    ]