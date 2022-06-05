from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.abstracts.cycle_dependents import CycleDependentAbstract
from kikeou.models.abstracts.person_dependents import PersonDependentAbstract

__all__ = ["Person", "Greeter", "LocationContact", "Programmer", "StageManager"]


class Person(CycleDependentAbstract):
    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    UNDEFINED = "undefined"
    ADULT = "adult"
    CHILD = "child"
    TEENAGER = "teenager"
    AGE_TYPES = (
        (UNDEFINED, _("undefined")),
        (ADULT, _("adult")),
        (CHILD, _("child")),
        (TEENAGER, _("teenager")),
    )

    OMNIVORE = "omnivore"
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    DIET_TYPES = (
        (OMNIVORE, _("omnivore")),
        (VEGETARIAN, _("vegetarian")),
        (VEGAN, _("vegan")),
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="persons",
        verbose_name=_("user"),
    )

    first_name = models.CharField(
        max_length=100, blank=False, verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("last name")
    )
    phone = models.CharField(max_length=50, blank=True, verbose_name=_("phone"))
    email = models.EmailField(blank=True, verbose_name=_("email"))
    age_type = models.CharField(
        default=UNDEFINED, max_length=9, choices=AGE_TYPES, verbose_name=_("age type")
    )
    diet_type = models.CharField(
        default=OMNIVORE, max_length=10, choices=DIET_TYPES, verbose_name=_("diet type")
    )
    diet_allergies = models.TextField(
        blank=True, verbose_name=_("allergies / intolerances")
    )

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name.strip()} {self.last_name.strip()}".strip()


class Greeter(PersonDependentAbstract):
    class Meta:
        verbose_name = _("greeter person")
        verbose_name_plural = _("greeter persons")


class LocationContact(PersonDependentAbstract):
    class Meta:
        verbose_name = _("location contact")
        verbose_name_plural = _("location contacts")


class Programmer(PersonDependentAbstract):
    class Meta:
        verbose_name = _("programmer person")
        verbose_name_plural = _("programmer persons")


class StageManager(PersonDependentAbstract):
    class Meta:
        verbose_name = _("stage manager")
        verbose_name_plural = _("stage managers")
