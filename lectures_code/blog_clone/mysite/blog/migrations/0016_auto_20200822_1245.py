# Generated by Django 3.1 on 2020-08-22 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200822_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 7, 15, 49, 565359, tzinfo=utc)),
        ),
    ]
