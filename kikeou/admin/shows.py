from django.contrib import admin

from ..models.shows import Show, ShowType

__all__ = ["ShowAdmin", "ShowTypeAdmin"]


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass


@admin.register(ShowType)
class ShowTypeAdmin(admin.ModelAdmin):
    pass
