from django.db import models
from django.utils.translation import ugettext_lazy as _

from kikeou.models.cycles import Cycle

__all__ = ["CycleDependentAbstract", "CycleDependentManager"]


class CycleDependentManager(models.Manager):
    def create(self, **kwargs):
        if "cycle" not in kwargs.keys():
            kwargs["cycle"] = self.get_default_cycle()
        return super().create(**kwargs)

    @classmethod
    def get_default_cycle(cls):
        # That will raise a Cycle.DoesNotExist exception in case of no cycle exists
        return Cycle.objects.get_active()


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
        default=CycleDependentManager.get_default_cycle,
    )
