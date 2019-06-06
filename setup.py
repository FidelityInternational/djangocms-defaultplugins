from setuptools import find_packages, setup

import djangocms_defaultplugins


INSTALL_REQUIREMENTS = ["Django>=1.11,<2.0", "django-cms>=3.5.0"]


setup(
    name="djangocms-defaultplugins",
    packages=find_packages(),
    include_package_data=True,
    version=djangocms_defaultplugins.__version__,
    description=djangocms_defaultplugins.__doc__,
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author="Fidelity International",
    url="https://github.com/FidelityInternational/djangocms-defaultplugins",
    license="BSD",
    test_suite="tests.settings.run",
)
