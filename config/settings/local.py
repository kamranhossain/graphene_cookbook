from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nhti9br-zet&3td#g1ui(e9(bl%#_pj30h@6ayyl)ayaz0@4vs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)
