from django.contrib import admin

from ..models import Cycle


__all__ = ["CycleAdmin"]


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    pass
