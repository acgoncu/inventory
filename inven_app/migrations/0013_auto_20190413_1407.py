# Generated by Django 2.1.4 on 2019-04-13 19:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inven_app', '0012_auto_20190311_1445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='PRequest',
        ),
    ]
