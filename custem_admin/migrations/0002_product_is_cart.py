# Generated by Django 4.0.6 on 2022-08-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custem_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_cart',
            field=models.BooleanField(default=False),
        ),
    ]