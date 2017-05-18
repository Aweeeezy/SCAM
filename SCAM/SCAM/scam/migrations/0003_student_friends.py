# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-18 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scam', '0002_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_student_friends_+', to='scam.Student'),
        ),
    ]