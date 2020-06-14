"""
Views for the wagtail admin dashbaord.
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .icon import BAKERY_ICON
from django.core import management


def index(request):
    return render(request, 'wagtailbakery/index.html', {'bakery_icon': BAKERY_ICON})


def publish(request):
    management.call_command(
        "build",
        skip_static=True,
        skip_media=True
    )
    management.call_command(
        "build",
        aws_bucket_name=settings.AWS_BAKERY_BUCKET_NAME,
        no_delete=True
    )

    return HttpResponse(_("Site has been published."))
