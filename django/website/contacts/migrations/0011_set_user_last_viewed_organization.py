# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def set_default_last_viewed_organization(apps, schema_editor):
    Organization = apps.get_model('organizations', 'Organization')
    User = apps.get_model('contacts', 'User')
    organization = Organization.objects.first()
    import rpdb2
    rpdb2.start_embedded_debugger("abc")
    for user in User.objects.all():
        user._preferences.last_viewed_organization = organization
        user._preferences.save()



class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_userpreferences_last_viewed_organization'),
    ]

    operations = [
        migrations.RunPython(set_default_last_viewed_organization),
    ]
