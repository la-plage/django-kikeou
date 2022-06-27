#!/usr/bin/env python

from _boot_django import boot_django
from django.core.management import call_command

boot_django()
call_command("collectstatic", "--no-input")
call_command("runserver", "0.0.0.0:8888")
