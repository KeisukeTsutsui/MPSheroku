# Generated by Django 3.1 on 2021-01-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstScreen', '0006_auto_20210112_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='font_size',
            field=models.CharField(choices=[('1', '小'), ('2', '中'), ('3', '大')], default='1', max_length=1),
        ),
    ]
