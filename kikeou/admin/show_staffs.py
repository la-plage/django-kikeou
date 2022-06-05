from django.contrib import admin

from ..models.show_staffs import ShowStaffFunction, ShowStaffMember

__all__ = ["ShowStaffFunctionAdmin", "ShowStaffMemberAdmin"]


@admin.register(ShowStaffFunction)
class ShowStaffFunctionAdmin(admin.ModelAdmin):
    pass


@admin.register(ShowStaffMember)
class ShowStaffMemberAdmin(admin.ModelAdmin):
    pass
