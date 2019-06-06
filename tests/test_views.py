from django.test.utils import override_settings

from cms.models import PageContent
from cms.test_utils.testcases import CMSTestCase
from cms.utils.plugins import downcast_plugins


@override_settings(
    CMS_PLACEHOLDER_CONF={
        "fullwidth.html content": {
            "default_plugins": [
                {
                    "plugin_type": "TextPlugin",
                    "values": {"body": "Top-level plugin"},
                    "children": [
                        {
                            "plugin_type": "TextPlugin",
                            "values": {"body": "A nested plugin"},
                        }
                    ],
                }
            ]
        }
    }
)
class HandlersTestCase(CMSTestCase):
    def test_populating_plugins(self):
        self.assertFalse(PageContent.objects.exists())

        with self.login_user_context(self.get_superuser()):
            self.client.post(
                self.get_page_add_uri("en"),
                {"title": "Test page", "slug": "test-page", "parent_node": ""},
            )

        self.assertEqual(PageContent.objects.count(), 1)

        page_content = PageContent.objects.get()
        placeholder = page_content.get_placeholders().get(slot="content")

        self.assertEqual(
            [plugin.body for plugin in downcast_plugins(placeholder.get_plugins_list())],
            ["Top-level plugin", "A nested plugin"],
        )
