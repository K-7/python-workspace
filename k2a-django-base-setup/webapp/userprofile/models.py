from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.models import BaseModel
from tenant.models import Tenant, Branch


class TenantUser(AbstractUser):
    phno = PhoneNumberField(null=True)
    tenant = models.ForeignKey(Tenant, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "tenant_user"

    def get_full_name(self):
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.email


class UserProfile(BaseModel):
    tenant_branch = models.ForeignKey(Branch)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=40, default="")
    last_name = models.CharField(max_length=40, default="")

    phno = PhoneNumberField(null=True)
    zipcode = models.CharField(max_length=255, default="")
    address = models.TextField(blank=True, default="")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")


    class Meta:
        db_table = "userprofile"

    def get_full_name(self):
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email