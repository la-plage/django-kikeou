from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.abstracts.cycle_dependents import CycleDependentAbstract
from kikeou.models.companies import Company
from kikeou.models.locations import Accommodation, Lodge, WarmUpPlace

__all__ = ["Show", "ShowType"]


class ShowType(CycleDependentAbstract):
    class Meta:
        verbose_name = _("show type")
        verbose_name_plural = _("show types")

    name = models.CharField(max_length=20, blank=False, verbose_name=_("name"))

    def __str__(self):
        return self.name


# Note that Show is related to a cycle via company foreign key
class Show(models.Model):
    class Meta:
        verbose_name = _("show")
        verbose_name_plural = _("shows")

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=False,
        related_name="shows",
        verbose_name=_("company"),
    )

    type = models.ForeignKey(
        ShowType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("show type"),
    )

    code = models.CharField(max_length=15, blank=True, verbose_name=_("code"))
    name = models.CharField(max_length=100, blank=False, verbose_name=_("name"))
    size = models.CharField(blank=True, max_length=20, verbose_name=_("size"))
    accessories = models.TextField(blank=True, verbose_name=_("accessories"))
    storage = models.TextField(blank=True, verbose_name=_("storage"))

    show_duration = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("show duration (minutes)")
    )
    setup_duration = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("setup duration (minutes)")
    )

    roadmap_remarks = models.TextField(blank=True, verbose_name=_("roadmap remarks"))
    info_sheet_remarks = models.TextField(
        blank=True, verbose_name=_("information sheet remarks")
    )

    # GREETER RELATED FIELDS --------------------------------------------------

    greeter = models.ForeignKey(
        "Greeter",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="shows",
        verbose_name=_("greeter"),
    )
    greeter_remarks = models.TextField(blank=True, verbose_name=_("greeter remarks"))
    food_remarks = models.TextField(blank=True, verbose_name=_("food remarks"))
    default_staff_arrival = models.DateTimeField(
        null=True, blank=True, verbose_name=_("staff arrival time (default)")
    )
    arrival_remarks = models.TextField(blank=True, verbose_name=_("arrival remarks"))
    last_minute_arrival = models.BooleanField(
        null=False, default=False, verbose_name=_("last minute arrival")
    )
    default_staff_departure = models.DateTimeField(
        null=True, blank=True, verbose_name=_("staff departure (default)")
    )
    MOTORIZED_VEHICLE = "motorized"
    WALKER = "walker"
    MEAN_OF_TRAVEL_TYPES = (
        (MOTORIZED_VEHICLE, _("motorized vehicle")),
        (WALKER, _("walker")),
    )
    mean_of_travel = models.CharField(
        choices=MEAN_OF_TRAVEL_TYPES,
        default="",
        max_length=9,
        blank=True,
        verbose_name=_("mean of travel"),
    )
    vehicles = models.TextField(blank=True, verbose_name=_("vehicles"))

    # ACCOMMODATION RELATED FIELDS --------------------------------------------

    default_accommodation = models.ForeignKey(
        Accommodation,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="shows",
        verbose_name=_("accommodation (default)"),
    )
    accommodation_remarks = models.TextField(
        blank=True, verbose_name=_("accommodation remarks")
    )

    # PROGRAMMER RELATED FIELDS -----------------------------------------------

    programmer = models.ForeignKey(
        "Programmer",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="shows",
        verbose_name=_("programmer"),
    )
    programmer_remarks = models.TextField(
        blank=True, verbose_name=_("programmer remarks")
    )

    # STAGE MANAGER RELATED FIELDS --------------------------------------------

    stage_manager = models.ForeignKey(
        "StageManager",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="shows_as_stage_manager",
        verbose_name=_("stage manager"),
    )
    stage_manager_remarks = models.TextField(
        blank=True, verbose_name=_("stage manager remarks")
    )

    # LODGE RELATED FIELDS ----------------------------------------------------

    need_lodge = models.BooleanField(
        null=True, default=None, verbose_name=_("need lodge")
    )
    lodge_people = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("people in lodge")
    )
    lodge_duration_before = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("time in lodge before the show (minutes)")
    )
    lodge_duration_after = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name=_("time in lodge after the show (minutes)")
    )
    need_lodge_catering = models.BooleanField(
        null=True, default=None, verbose_name=_("catering in lodge")
    )
    default_lodge = models.ForeignKey(
        Lodge,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="shows",
        verbose_name=_("lodge (default)"),
    )
    lodge_remarks = models.TextField(blank=True, verbose_name=_("lodge remarks"))

    # WARM UP RELATED FIELDS --------------------------------------------------

    need_warm_up = models.BooleanField(
        null=True, default=None, verbose_name=_("need warm up")
    )
    warm_up_duration = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=_("warm up duration (minutes)")
    )
    warm_up_spaces_remarks = models.TextField(
        blank=True, verbose_name=_("warm up spaces remarks")
    )
    default_warm_up_place = models.ForeignKey(
        WarmUpPlace,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="warm_up_shows",
        verbose_name=_("warm up place (default)"),
    )

    def __str__(self):
        if self.code:
            return f"[{self.code}] {self.name}"
        return self.name
