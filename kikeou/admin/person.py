from django.contrib import admin

from ..models import Person

__all__ = ["PersonAdmin"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
