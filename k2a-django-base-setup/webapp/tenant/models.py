from __future__ import unicode_literals

from django.db import models

from core.models import BaseModel


class Tenant(BaseModel):
    TENANT_TYPE = (
        ('HOTEL', 'HOTEL'),
        ('RETAILERS', 'RETAILERS'),
    )
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=50, choices=TENANT_TYPE)

    class Meta:
        db_table = "tenant"

    def __unicode__(self):
        return self.name



class Branch(BaseModel):
    tenant = models.ForeignKey(Tenant)
    name = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length=255, default="")
    address = models.TextField(blank=True, default="")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")


    class Meta:
        db_table = "branch"

    def __unicode__(self):
        return self.name