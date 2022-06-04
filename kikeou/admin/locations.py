from django.contrib import admin

from ..models.locations import Accommodation, Location, Lodge, Stage, WarmUpPlace

__all__ = [
    "AccommodationAdmin",
    "LocationAdmin",
    "LodgeAdmin",
    "StageAdmin",
    "WarmUpPlaceAdmin",
]


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Lodge)
class LodgeAdmin(admin.ModelAdmin):
    pass


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass


@admin.register(WarmUpPlace)
class WarmUpPlaceAdmin(admin.ModelAdmin):
    pass
