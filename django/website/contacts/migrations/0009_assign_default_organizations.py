# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


def set_default_organisation_owner(apps, schema_editor):
    Organization = apps.get_model('organizations', 'Organization')
    OrganizationOwner = apps.get_model('organizations', 'OrganizationOwner')
    OrganizationUser = apps.get_model('organizations', 'OrganizationUser')
    User = apps.get_model('contacts', 'User')
    if User.objects.exists():
        default_org = Organization.objects.get(name=settings.DEFAULT_ORGANIZATION_NAME)
        user = User.objects.order_by('id')[0]
        org_user = OrganizationUser.objects.get(user=user, organization=default_org)
        org_user.is_admin = True
        org_user.save()
        OrganizationOwner.objects.create(organization_user=org_user, organization=default_org)


def add_existing_users_to_default_organization(apps, schema_editor):
    Organization = apps.get_model('organizations', 'Organization')
    OrganizationUser = apps.get_model('organizations', 'OrganizationUser')
    User = apps.get_model('contacts', 'User')
    if Organization.objects.exists():
        default_org = Organization.objects.get(name=settings.DEFAULT_ORGANIZATION_NAME)
    else:
        default_org = False
    if default_org:
        for user in User.objects.all():
            OrganizationUser.objects.create(user=user, organization=default_org)


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_nameonlypermission'),
        ('logframe', '0012_auto_20170222_1614'),
    ]

    operations = [
        migrations.RunPython(add_existing_users_to_default_organization),
        migrations.RunPython(set_default_organisation_owner)
    ]
