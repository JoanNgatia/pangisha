# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Building(models.Model):
    """Building details."""

    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=250, default='Nairobi')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class House(models.Model):
    CATEGORY_CHOICES = (
        ('Bedsitter', 'Bedsitter'),
        ('1 Bedroom', '1 Bedroom'),
        ('2 Bedroom', '2 Bedroom'),
        ('Shop', 'Shop'),
    )
    house_type = models.CharField(max_length=15, blank=True, choices=CATEGORY_CHOICES)
    description = models.TextField()
    rent_expected = models.CharField(max_length=6)
    building = models.ForeignKey(
        Building, related_name='houses', on_delete=models.CASCADE)
    number = models.CharField(max_length=3)

    def __str__(self):
        return self.number


class Tenant(models.Model):

    name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now=True)
    current_space = models.ForeignKey(House, on_delete=models.CASCADE, related_name='tenant', null=True)

    def __str__(self):
        return self.name

