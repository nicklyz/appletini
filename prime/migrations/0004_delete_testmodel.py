# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_testmodel_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
