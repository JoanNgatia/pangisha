# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Building, Tenant, House

admin.site.register(Building)
admin.site.register(Tenant)
admin.site.register(House)
