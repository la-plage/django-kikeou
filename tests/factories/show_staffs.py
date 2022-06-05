import factory

from kikeou.models.show_staffs import ShowStaffFunction, ShowStaffMember
from tests import factories

__all__ = ["ShowStaffFunctionFactory", "ShowStaffMemberFactory"]


class ShowStaffFunctionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowStaffFunction

    name = factory.Sequence(lambda n: f"staff function #{n}")


class ShowStaffMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowStaffMember

    person = factory.SubFactory(
        factories.PersonFactory,
        first_name=factory.Sequence(lambda n: f"Show staff member #{n}"),
    )
    show = factory.SubFactory(factories.ShowFactory)
    staff_function = factory.SubFactory(ShowStaffFunctionFactory)
