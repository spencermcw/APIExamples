from __future__ import unicode_literals

from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=25)
    walker = models.ForeignKey('Person', models.DO_NOTHING, db_column='walker', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dog'


class Person(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'person'
