# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel
from django.conf import settings


# @python_2_unicode_compatible
class Order(TimeStampedModel):
    payer = models.ForeignKey(settings.AUTH_USER_MODEL)
    price = models.SmallIntegerField()  # Price in cents
    created_at = models.DateTimeField()


@python_2_unicode_compatible
class RentType(TimeStampedModel):
    name = models.CharField()
    days = models.PositiveSmallIntegerField()
    price = models.SmallIntegerField()  # Price in cents

    def __str__(self):
        return self.name


# @python_2_unicode_compatible
class Rent(TimeStampedModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    bike = models.ForeignKey('bikes.Bike')
    rent_type = models.ForeignKey('RentType')
    order = models.ForeignKey('Order')
