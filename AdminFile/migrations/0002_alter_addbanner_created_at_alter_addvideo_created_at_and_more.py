# Generated by Django 4.1.5 on 2023-04-27 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminFile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbanner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 12, 55, 36, 332642), null=True),
        ),
        migrations.AlterField(
            model_name='addvideo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 12, 55, 36, 332642), null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 12, 55, 36, 331642), null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 12, 55, 36, 330642), null=True),
        ),
    ]
