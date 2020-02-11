# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Building, House


class ModelTestCase(TestCase):
    """Define correct model creation."""

    def setUp(self):
        """Add initial data."""
        self.owner = 'J'
        self.new_building = Building(owner=self.owner)

    def test_new_model_creation(self):
        """Check new model instantiation."""
        initial_count = Building.objects.count()
        self.new_building.save()
        new_count = Building.objects.count()
        self.assertNotEqual(initial_count, new_count)

        self.number = 'B7'
        self.new_house = House(
            number=self.number, building=self.new_building)
        self.new_house.save()
        self.assertEqual(len(House.objects.all()), 1)
