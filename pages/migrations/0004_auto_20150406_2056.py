# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150406_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 20, 56, 40, 340235, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
    ]
