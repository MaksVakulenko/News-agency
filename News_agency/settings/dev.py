from News_agency.settings.base import *

SECRET_KEY = "django-insecure-bs_93dqj7=e1it0j5bz2ix3_5*uc(s8+$pwafymy444_#2$a42"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}