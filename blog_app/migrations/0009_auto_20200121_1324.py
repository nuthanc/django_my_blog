# Generated by Django 2.2.1 on 2020-01-21 13:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20200120_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 21, 13, 24, 34, 282768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 21, 13, 24, 34, 282375, tzinfo=utc)),
        ),
    ]
