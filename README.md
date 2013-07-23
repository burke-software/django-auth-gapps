Based on http://peterkropf.com/archives/13

A simple way to authenticate to Google Apps using the provisioning API. If you want oath to allow any Google user to login look elsewhere.

This is more like a Google Apps version of django-auth-ldap. It supports Group mappings as well.


# Installation
pip install django-auth-gapps

In settings.py

```
GAPPS_DOMAIN = 'mydomain.com'
GAPPS_USERNAME = ''  # Just the username, no @
GAPPS_PASSWORD = ''
# Check for new groups, or only on initial user creation
GAPPS_ALWAY_ADD_GROUPS = False
AUTHENTICATION_BACKENDS += ('google_auth.backends.GoogleAppsBackend',)
```

Add 'google_auth' to installed_apps

Add to urls.py patterns('', (r'^accounts/login/$', 'google_auth.views.login'), )

syncdb

You can set up group mappings in /admin if you want.
