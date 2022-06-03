from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models import Cycle

__all__ = ["Person"]


class PersonManager(models.Manager):
    def create(self, **kwargs):
        kwargs.update(
            {
                "cycle": Cycle.objects.get_active(),
            }
        )
        return super().create(**kwargs)


class Person(models.Model):
    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    objects = PersonManager()

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

    cycle = models.ForeignKey(
        Cycle,
        on_delete=models.PROTECT,
        related_name="persons",
        verbose_name=_("cycle"),
        editable=False,
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

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name.strip()} {self.last_name.strip()}".strip()

    def save(self, *args, **kwargs):
        try:
            _ = self.cycle
        except Cycle.DoesNotExist:
            self.cycle = Cycle.objects.get_active()
        super().save(*args, **kwargs)
