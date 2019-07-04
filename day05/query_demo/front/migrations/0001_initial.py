# Generated by Django 2.1 on 2019-06-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'book',
                'ordering': [],
            },
        ),
    ]
