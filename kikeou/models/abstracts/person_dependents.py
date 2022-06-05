from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    "PersonDependentAbstract",
    "PersonDependentManager",
    "PersonDependentToManyAbstract",
]


class PersonDependentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("person")


class PersonDependentAbstract(models.Model):
    class Meta:
        abstract = True

    objects = PersonDependentManager()

    person = models.OneToOneField(
        "Person",
        on_delete=models.CASCADE,
        verbose_name=_("person"),
        related_name="%(class)s",
        null=False,
    )

    def __str__(self):
        return str(self.person)


class PersonDependentToManyAbstract(PersonDependentAbstract):
    """
    Same than PersonDependentAbstract but replace the person OneToOneField with ForeignKey
    """

    class Meta:
        abstract = True

    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE,
        verbose_name=_("person"),
        related_name="%(class)s_set",
        null=False,
    )
