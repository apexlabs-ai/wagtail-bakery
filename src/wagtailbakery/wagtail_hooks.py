from django.urls import include, reverse
from django.urls import path
from django.utils.translation import gettext_lazy as _
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from .icon import BAKERY_ICON
from .urls import urlpatterns


class BakeryMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('bakery/', include((urlpatterns, 'wagtailbakery'), namespace='wagtailbakery_admin')),
    ]


@hooks.register('register_settings_menu_item')
def register_bakery_menu():
    return BakeryMenuItem(
        _('Bakery'),
        reverse('wagtailbakery_admin:index'),
        classnames='icon icon-' + BAKERY_ICON)
