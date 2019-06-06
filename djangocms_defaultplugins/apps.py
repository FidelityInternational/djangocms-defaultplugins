from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DefaultPluginsConfig(AppConfig):
    name = "djangocms_defaultplugins"
    verbose_name = _("django CMS Default Plugins")

    def ready(self):
        from . import handlers
