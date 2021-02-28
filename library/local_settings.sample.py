# SECURITY WARNING: keep the secret key used in production secret!
# Set secure string as SECRET_KEY.
SECRET_KEY = 'Your desire SECRET_KEY'

# Set your personal database information.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your database name',
        'USER': 'Your database user',
        'PASSWORD': 'Your database password',
    }
}
