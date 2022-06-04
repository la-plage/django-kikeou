from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.cycles import Cycle

__all__ = ["CycleDependentAbstract", "CycleDependentManager"]


def get_default_cycle():
    # That will raise a Cycle.DoesNotExist exception in case no cycle exists
    return Cycle.objects.get_active()


class CycleDependentManager(models.Manager):
    def create(self, **kwargs):
        if "cycle" not in kwargs.keys():
            kwargs["cycle"] = get_default_cycle()
        return super().create(**kwargs)


class CycleDependentAbstract(models.Model):
    class Meta:
        abstract = True

    objects = CycleDependentManager()

    cycle = models.ForeignKey(
        Cycle,
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        verbose_name=_("cycle"),
        editable=False,
        default=get_default_cycle,
    )
