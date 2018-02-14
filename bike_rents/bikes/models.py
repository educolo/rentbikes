# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Bike(TimeStampedModel):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=30)
    size = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{name} {model}".format(name=self.name, model=self.model)
