# Generated by Django 3.2.13 on 2022-06-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kikeou", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="age_type",
            field=models.CharField(
                choices=[
                    ("undefined", "undefined"),
                    ("adult", "adult"),
                    ("child", "child"),
                    ("teenager", "teenager"),
                ],
                default="undefined",
                max_length=9,
                verbose_name="age type",
            ),
        ),
    ]
