from setuptools import setup, find_packages

setup(
    name = "django-auth-gapps",
    version = "1.0",
    author = "David Burke",
    author_email = "david@burkesoftware.com",
    description = ("Authentication with Google Apps Provisioning api"),
    license = "BSD",
    keywords = "django",
    url = "http://code.google.com/p/django-auth-gapps/",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['gdata']
)
