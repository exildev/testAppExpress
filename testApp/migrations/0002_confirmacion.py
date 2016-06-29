# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pedido', models.IntegerField()),
                ('motorizado', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'Confirmacion',
                'verbose_name_plural': 'Confirmaciones',
            },
        ),
    ]
