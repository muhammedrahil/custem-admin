# Generated by Django 4.0.6 on 2022-08-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
                ('description', models.CharField(default='', max_length=250)),
                ('image', models.ImageField(upload_to='upload_image')),
            ],
        ),
    ]
