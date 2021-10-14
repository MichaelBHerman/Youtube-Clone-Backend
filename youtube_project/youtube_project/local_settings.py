# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-29+o9x%t@f16n+awotitq#xk-$795_f!!2v5!#^5uz&&w(hwza'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_comment_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
