# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151005_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='category',
        ),
    ]
