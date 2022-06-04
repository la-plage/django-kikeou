from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.abstracts.cycle_dependents import CycleDependentAbstract
from kikeou.models.abstracts.location_dependents import LocationDependentAbstract
from kikeou.models.persons import LocationContact

__all__ = ["Accommodation", "Location", "Lodge", "Stage", "WarmUpPlace"]


class Location(CycleDependentAbstract):
    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    name = models.CharField(max_length=50, blank=False, verbose_name=_("name"))
    street = models.CharField(max_length=100, blank=True, verbose_name=_("street & n°"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("zip code"))
    city = models.CharField(max_length=50, blank=True, verbose_name=_("city"))

    contact = models.ForeignKey(
        LocationContact,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="locations",
        verbose_name=_("lodge contact"),
    )

    def __str__(self):
        return self.name


class Accommodation(LocationDependentAbstract):
    class Meta:
        verbose_name = _("accommodation")
        verbose_name_plural = _("accommodations")


class Lodge(LocationDependentAbstract):
    class Meta:
        verbose_name = _("lodge")
        verbose_name_plural = _("lodges")

    gauge = models.PositiveSmallIntegerField(default=0, verbose_name=_("gauge"))
    ground_floor = models.BooleanField(default=False, verbose_name=_("ground floor"))
    soundproofed = models.BooleanField(default=False, verbose_name=_("soundproofed"))


class WarmUpPlace(LocationDependentAbstract):
    class Meta:
        verbose_name = _("warm-up place")
        verbose_name_plural = _("warm-up places")


class Stage(LocationDependentAbstract):
    class Meta:
        verbose_name = _("stage")
        verbose_name_plural = _("stages")

    default_lodge = models.ForeignKey(
        Lodge,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="default_stage_assignations",
        verbose_name=_("default lodge"),
    )
    default_warming_up_place = models.ForeignKey(
        WarmUpPlace,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="default_stage_assignations",
        verbose_name=_("default warm up place"),
    )
