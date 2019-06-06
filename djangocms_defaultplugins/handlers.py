from django.dispatch import receiver

from cms.api import add_plugin
from cms.operations import ADD_PAGE_TRANSLATION
from cms.signals import post_obj_operation
from cms.utils.placeholder import get_placeholder_conf, rescan_placeholders_for_obj


def _create_default_plugins(placeholder, language, confs, parent=None):
    for conf in confs:
        plugin = add_plugin(
            placeholder,
            conf["plugin_type"],
            language,
            target=parent,
            **conf["values"]
        )
        if "children" in conf:
            _create_default_plugins(placeholder, language, conf["children"], plugin)


@receiver(post_obj_operation)
def populate_default_plugins(sender, operation, request, **kwargs):
    if operation != ADD_PAGE_TRANSLATION:
        return
    page, language = kwargs["obj"], kwargs["language"]
    page_content = page.get_title_obj(language)

    # create placeholders
    rescan_placeholders_for_obj(page_content)

    for placeholder in page_content.get_placeholders():
        _create_default_plugins(
            placeholder,
            language,
            get_placeholder_conf(
                "default_plugins",
                placeholder.slot,
                page_content.get_template(),
                default=[],
            ),
        )
