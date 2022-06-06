# Generated by Django 3.2.13 on 2022-06-06 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kikeou", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="locations",
                to="kikeou.locationcontact",
                verbose_name="contact",
            ),
        ),
    ]
