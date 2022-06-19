from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.abstracts.person_dependents import PersonDependentToManyAbstract
from kikeou.models.locations import Accommodation


class ShowStaffFunction(models.Model):
    class Meta:
        verbose_name = _("staff function")
        verbose_name_plural = _("staff functions")

    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class ShowStaffMember(PersonDependentToManyAbstract):
    class Meta:
        verbose_name = _("staff member")
        verbose_name_plural = _("staff members")

    show = models.ForeignKey(
        "Show",
        on_delete=models.CASCADE,
        related_name="staff_persons",
        verbose_name=_("show"),
    )
    staff_function = models.ForeignKey(
        ShowStaffFunction,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="staff_members",
        verbose_name=_("staff function"),
    )
    comments = models.TextField(blank=True, verbose_name=_("comments"))
    is_present = models.BooleanField(default=True, verbose_name=_("is present"))
    is_contact_person = models.BooleanField(
        default=False, verbose_name=_("contact person")
    )
    approximate_time_of_arrival = models.BooleanField(
        default=False, verbose_name=_("approximate time of arrival")
    )
    arrival = models.DateTimeField(null=True, blank=True, verbose_name=_("arrival"))
    departure = models.DateTimeField(null=True, blank=True, verbose_name=_("departure"))
    need_accommodations = models.BooleanField(
        null=True, default=None, verbose_name=_("need accommodations")
    )
    accommodation_place = models.ForeignKey(
        Accommodation,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="persons",
        verbose_name=_("accommodation place"),
    )
    accommodation_comments = models.TextField(
        blank=True, verbose_name=_("accommodation comments")
    )
