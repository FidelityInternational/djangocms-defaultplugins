.. djangocms-defaultplugins documentation master file, created by
   sphinx-quickstart on Thu Feb 14 11:45:02 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to djangocms-defaultplugins's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Overview
--------

Django CMS Default Plugins provides a way to automatically populate
placeholders with plugins.

Installation
------------

Run::

    pip install djangocms-defaultplugins

Add ``djangocms_defaultplugins`` to your project's ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'djangocms_defaultplugins',
        # ...
    ]

Configuration
-------------

Default Plugins uses an additional key in ``CMS_PLACEHOLDER_CONF`` configuration:

.. _placeholder_default_plugins:

``default_plugins``
    You can specify the list of default plugins which will be automatically
    added when the placeholder will be created (or rendered).
    Each element of the list is a dictionary with following keys :

    ``plugin_type``
        The plugin type to add to the placeholder
        Example : ``TextPlugin``

    ``values``
        Dictionary to use for the plugin creation.
        It depends on the ``plugin_type``. See the documentation of each
        plugin type to see which parameters are required and available.
        Example for a text plugin:
        ``{'body':'<p>Lorem ipsum</p>'}``
        Example for a link plugin:
        ``{'name':'Django-CMS','url':'https://www.django-cms.org'}``

    ``children``
        It is a list of dictionaries to configure default plugins
        to add as children for the current plugin (it must accepts children).
        Each dictionary accepts same args than dictionaries of
        ``default_plugins`` : ``plugin_type``, ``values``, ``children``
        (yes, it is recursive).

    Complete example of default_plugins usage::

        CMS_PLACEHOLDER_CONF = {
            'content': {
                'name' : _('Content'),
                'plugins': ['TextPlugin', 'LinkPlugin'],
                'default_plugins':[
                    {
                        'plugin_type':'TextPlugin',
                        'values':{
                            'body':'<p>Great websites : %(_tag_child_1)s and %(_tag_child_2)s</p>'
                        },
                        'children':[
                            {
                                'plugin_type':'LinkPlugin',
                                'values':{
                                    'name':'django',
                                    'url':'https://www.djangoproject.com/'
                                },
                            },
                            {
                                'plugin_type':'LinkPlugin',
                                'values':{
                                    'name':'django-cms',
                                    'url':'https://www.django-cms.org'
                                },
                                # If using LinkPlugin from djangocms-link which
                                # accepts children, you could add some grandchildren :
                                # 'children' : [
                                #     ...
                                # ]
                            },
                        ]
                    },
                ]
            }
        }


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
