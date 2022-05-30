from django.db import models, transaction
from django.db.models import Q, UniqueConstraint
from django.utils.translation import ugettext_lazy as _

__all__ = ["Cycle"]


class Cycle(models.Model):
    """
    A cycle can be a festival edition, club season, ...
    """

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["is_the_active_one"],
                condition=Q(is_the_active_one=True),
                name="unique_is_the_active_one",
            )
        ]
        verbose_name = _("cycle")
        verbose_name_plural = _("cycles")

    is_the_active_one = models.BooleanField(
        default=False, verbose_name=_("is the active one")
    )
    name = models.CharField(max_length=100, blank=False, verbose_name=_("name"))
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("end date"))

    def save(self, *args, **kwargs):
        if self.end_date < self.start_date:
            raise ValueError(_("End date can't be before start date"))

        # if we create first record, force is_the_active_one = True
        is_first_cycle_record = not type(self).objects.all().count()
        if is_first_cycle_record:
            self.is_the_active_one = True
        with transaction.atomic():
            if self.is_the_active_one and not is_first_cycle_record:
                type(self).objects.filter(is_the_active_one=True).update(
                    is_the_active_one=False
                )
            super().save(*args, **kwargs)
