# Generated by Django 3.1 on 2021-01-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstScreen', '0008_auto_20210112_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='text',
            field=models.TextField(default='デフォルトのメッセージ', max_length=50),
        ),
    ]
