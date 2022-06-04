from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ["LocationDependentAbstract", "LocationDependentManager"]


class LocationDependentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("location")


class LocationDependentAbstract(models.Model):
    class Meta:
        abstract = True

    objects = LocationDependentManager()

    location = models.OneToOneField(
        "Location",
        on_delete=models.CASCADE,
        verbose_name=_("location"),
        related_name="%(class)s",
        null=False,
    )

    def __str__(self):
        return str(self.location)
