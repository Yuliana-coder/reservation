# Generated by Django 3.1.4 on 2020-12-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0007_auto_20201208_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
