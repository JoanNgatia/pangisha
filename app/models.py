# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Building(models.Model):
    """Building details."""

    owner = models.CharField(max_length=255)


class Tenant(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(max_length=20)


class House(models.Model):
    building = models.ForeignKey(
        Building, related_name='houses', on_delete=models.CASCADE)
    description = models.TextField()
    number = models.CharField(max_length=3)
    tenant = models.ForeignKey(
        Tenant, on_delete=models.SET_NULL, related_name='tenants', null=True)
    rent_expected = models.CharField(max_length=6)
