# Generated by Django 3.0.6 on 2021-01-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('screenshot', models.ImageField(upload_to='Project Images')),
                ('bio', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
            ],
        ),
    ]
