# Generated by Django 3.0.6 on 2021-01-28 07:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_auto_20210128_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='web_host_provider',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='web_host_type',
            field=models.CharField(choices=[('Cloud', 'Cloud'), ('VPS', 'VPS'), ('Shared Hosting', 'Shared Hosting')], default='Cloud', max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 7, 41, 59, 327274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 7, 41, 59, 325977, tzinfo=utc)),
        ),
    ]