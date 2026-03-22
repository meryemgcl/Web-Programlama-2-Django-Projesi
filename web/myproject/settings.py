import os
from pathlib import Path

# Proje ana dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK UYARISI: Bu anahtarı üretim ortamında gizli tutun!
SECRET_KEY = 'django-insecure-+!im#5f0w)!qr8qv@+i1a_2sd1@0z9x7kz&bu_bvxkvpml@se0'

# GÜVENLİK UYARISI: Üretim ortamında DEBUG'ı kapatmayı unutmayın!
DEBUG = True

ALLOWED_HOSTS = []

# Uygulama Tanımlamaları
INSTALLED_APPS = [
    'polls.apps.PollsConfig',  # Kendi uygulaman
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Ana dizindeki templates klasörü
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Medya dosyalarına şablonlardan erişebilmek için:
                'django.template.context_processors.media', 
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Veritabanı (Varsayılan SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre Doğrulama
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Yerelleştirme (Türkiye Ayarları)
LANGUAGE_CODE = 'tr-tr' 

TIME_ZONE = 'Europe/Istanbul' 

USE_I18N = True

USE_TZ = True

# Statik Dosyalar (CSS, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# --- YENİ EKLENEN KISIM: MEDYA DOSYALARI (RESİMLER) ---
# Kullanıcıların yüklediği resimlerin URL ve dosya yolu ayarları
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'