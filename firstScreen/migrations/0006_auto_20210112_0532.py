# Generated by Django 3.1 on 2021-01-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstScreen', '0005_auto_20210112_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='ballon_type',
            field=models.CharField(choices=[('1', '左下'), ('2', '左上'), ('3', '右下'), ('4', '右上')], default='1', max_length=1),
        ),
    ]
