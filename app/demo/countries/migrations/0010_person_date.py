# Generated by Django 2.2.2 on 2019-07-08 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0009_auto_20190702_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 8, 15, 28, 7, 931019), verbose_name='Birth Date'),
            preserve_default=False,
        ),
    ]
