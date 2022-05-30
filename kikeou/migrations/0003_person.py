# Generated by Django 3.2.13 on 2022-05-30 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kikeou", "0002_auto_20220530_1051"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="last name"
                    ),
                ),
                (
                    "phone",
                    models.CharField(blank=True, max_length=50, verbose_name="phone"),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email"),
                ),
                (
                    "diet_type",
                    models.CharField(
                        choices=[
                            ("omnivore", "omnivore"),
                            ("vegetarian", "vegetarian"),
                            ("vegan", "vegan"),
                        ],
                        default="omnivore",
                        max_length=10,
                        verbose_name="diet type",
                    ),
                ),
                (
                    "diet_allergies",
                    models.TextField(
                        blank=True, verbose_name="allergies / intolerances"
                    ),
                ),
                (
                    "cycle",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="persons",
                        to="kikeou.cycle",
                        verbose_name="cycle",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="persons",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "persons",
            },
        ),
    ]