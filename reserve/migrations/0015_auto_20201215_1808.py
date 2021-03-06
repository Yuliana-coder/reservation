# Generated by Django 3.1.4 on 2020-12-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0014_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=800)),
                ('salary', models.IntegerField(default=20000)),
                ('duties', models.CharField(max_length=400)),
                ('demands', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
