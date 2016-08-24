# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_info', '0002_auto_20160811_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpinfo',
            name='p1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p1', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p10',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p10', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p2', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p3', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p4',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p4', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p5',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p5', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p6',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p6', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p7',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p7', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p8',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p8', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='p9',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_p9', to='bolao_info.PilotInfo'),
        ),
        migrations.AlterField(
            model_name='gpinfo',
            name='pole',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='gp_pole', to='bolao_info.PilotInfo'),
        ),
    ]
