# Generated by Django 3.1.4 on 2020-12-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('path', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'db_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('painting', models.CharField(blank=True, max_length=100, null=True)),
                ('path', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'db_painting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'db_user',
                'managed': False,
            },
        ),
    ]
