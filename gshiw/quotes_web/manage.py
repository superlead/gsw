#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    profile = os.environ.get('QUOTES_WEB_PROFILE', 'develop')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_web.settings.%s" % profile)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)