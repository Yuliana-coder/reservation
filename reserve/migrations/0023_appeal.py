# Generated by Django 3.1.4 on 2020-12-23 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0022_petitionreason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('petitionReason', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='reserve.petitionreason')),
            ],
        ),
    ]