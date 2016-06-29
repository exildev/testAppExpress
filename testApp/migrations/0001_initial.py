# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorizado',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=50)),
                ('identificador', models.CharField(max_length=50)),
                ('tipo', models.IntegerField(choices=[(1, b'suscrito'), (2, b'empleado')])),
                ('empresa', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Motorizado',
                'verbose_name_plural': 'Motorizados',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
