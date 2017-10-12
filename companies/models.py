# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin import models
from django.db import models



class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close= models.FloatField()
    volume= models.IntegerField()

    def __str__(self):

        return self.ticker

