# Generated by Django 2.2 on 2019-04-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190426_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.CharField(default='Nairobi', max_length=250),
        ),
    ]
