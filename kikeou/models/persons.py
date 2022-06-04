from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.utils.abstracts import CycleDependentAbstract

__all__ = ["Person", "Greeter", "LocationContact", "Programmer", "StageManager"]


class Person(CycleDependentAbstract):
    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    ADULT = "adult"
    CHILD = "child"
    TEENAGER = "teenager"
    AGE_TYPES = (
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
    diet_type = models.CharField(
        default=OMNIVORE, max_length=10, choices=DIET_TYPES, verbose_name=_("diet type")
    )
    diet_allergies = models.TextField(
        blank=True, verbose_name=_("allergies / intolerances")
    )

    is_greeter = models.BooleanField(default=False, verbose_name=_("is greeter"))
    is_location_contact = models.BooleanField(
        default=False, verbose_name=_("is location contact")
    )
    is_programmer = models.BooleanField(default=False, verbose_name=_("is programmer"))
    is_stage_manager = models.BooleanField(
        default=False, verbose_name=_("is stage manager")
    )

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name.strip()} {self.last_name.strip()}".strip()


class GreeterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_greeter=True)


class Greeter(Person):
    class Meta:
        proxy = True
        verbose_name = _("greeter person")
        verbose_name_plural = _("greeter persons")

    objects = GreeterManager()

    def save(self, *args, **kwargs):
        self.is_greeter = True
        super().save(*args, **kwargs)


class LocationContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_location_contact=True)


class LocationContact(Person):
    class Meta:
        proxy = True
        verbose_name = _("location contact")
        verbose_name_plural = _("location contacts")

    objects = LocationContactManager()

    def save(self, *args, **kwargs):
        self.is_location_contact = True
        super().save(*args, **kwargs)


class ProgrammerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_programmer=True)


class Programmer(Person):
    class Meta:
        proxy = True
        verbose_name = _("programmer person")
        verbose_name_plural = _("programmer persons")

    objects = ProgrammerManager()

    def save(self, *args, **kwargs):
        self.is_programmer = True
        super().save(*args, **kwargs)


class StageManagerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_stage_manager=True)


class StageManager(Person):
    class Meta:
        proxy = True
        verbose_name = _("stage manager")
        verbose_name_plural = _("stage managers")

    objects = StageManagerManager()

    def save(self, *args, **kwargs):
        self.is_stage_manager = True
        super().save(*args, **kwargs)
