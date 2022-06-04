from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.abstracts.cycle_dependents import CycleDependentAbstract

__all__ = ["Company"]


class Company(CycleDependentAbstract):
    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")

    name = models.CharField(max_length=100, blank=False, verbose_name=_("name"))

    def __str__(self):
        return self.name
