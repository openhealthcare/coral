"""
Admin for billing app
"""
from django.contrib import admin

from billing import models

admin.site.register(models.BillingItem, admin.ModelAdmin)
