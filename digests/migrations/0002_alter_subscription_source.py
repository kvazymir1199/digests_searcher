# Generated by Django 4.2.3 on 2023-07-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='source',
            field=models.CharField(max_length=200),
        ),
    ]
