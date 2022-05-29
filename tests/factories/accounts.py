from factory import PostGenerationMethodCall, Sequence
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model


__all__ = ["StaffUserFactory", "SuperUserFactory", "UserFactory"]


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = Sequence(lambda n: f"toto-{n}")
    password = PostGenerationMethodCall("set_password", "tutu")

    is_staff = False
    is_superuser = False
    is_active = True


class StaffUserFactory(UserFactory):
    is_staff = True


class SuperUserFactory(StaffUserFactory):
    is_superuser = True
