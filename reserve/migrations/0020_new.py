# Generated by Django 3.1.4 on 2020-12-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0019_order_quantityarray'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('articleTopic', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=800)),
                ('datePublication', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
