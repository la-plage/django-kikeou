from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cycle(models.Model):
    """
    A cycle can be a festival edition, club season, ...
    """

    class Meta:
        verbose_name = _("cycle")
        verbose_name_plural = _("cycles")

    name = models.CharField(max_length=100, blank=False, verbose_name=_("name"))
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("end date"))

    def save(self, *args, **kwargs):
        if self.end_date < self.start_date:
            raise ValueError(_("End date can't be before start date"))
        super().save(*args, **kwargs)
