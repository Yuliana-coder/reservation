# Generated by Django 3.1.4 on 2020-12-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=150)),
                ('orderTime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
