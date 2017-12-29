from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleType)
admin.site.register(models.Order)