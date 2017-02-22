# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_model_update'),
        ('logframe', '0008_auto_20160429_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='logframe',
            name='organization',
            field=models.ForeignKey(to='organizations.Organization', null=True),
        ),
    ]
