# Generated by Django 3.2.5 on 2022-07-06 19:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220706_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 6, 19, 36, 11, 952836, tzinfo=utc)),
        ),
    ]