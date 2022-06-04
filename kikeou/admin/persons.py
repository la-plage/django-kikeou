from django.contrib import admin

from ..models.persons import Greeter, LocationContact, Person, Programmer, StageManager

__all__ = [
    "PersonAdmin",
    "GreeterAdmin",
    "LocationContactAdmin",
    "ProgrammerAdmin",
    "StageManagerAdmin",
]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Greeter)
class GreeterAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationContact)
class LocationContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    pass


@admin.register(StageManager)
class StageManagerAdmin(admin.ModelAdmin):
    pass
