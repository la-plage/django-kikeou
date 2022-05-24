#!/usr/bin/env python

from django.core.management import call_command

from _boot_django import boot_django


boot_django()
call_command("makemigrations", "kikeou")
