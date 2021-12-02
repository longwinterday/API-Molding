from django.contrib import admin
from .models import Molding, Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Molding)
class MoldingAdmin(admin.ModelAdmin):
    pass
