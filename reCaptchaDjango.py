'''
    Created by : Cristian Steib
    date : 8/12/16
    necesitas agregar en el setting de tu proyecto lo siguiente:

    RECAPTCHA_SECRET_KEY = ' tu clave '

'''
from django.conf import settings
from . import reCaptcha


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

c = Colors()

def reCaptcha():
    try:
        return reCaptcha.reCaptcha(settings.RECAPTCHA_SECRET_KEY)
        print  c.FAIL + ' Tienes que definir en settings ' + c.OKGREEN + 'RECAPTCHA_SECRET_KEY="tu clave"' + c.FAIL
    except:
        return None

def sitekey():
    try:
        return settings.RECAPTCHA_SITE_KEY
    except:
        print  c.FAIL + ' Tienes que definir en settings ' + c.OKGREEN + 'RECAPTCHA_SITE_KEY="tu clave"' + c.FAIL
        return None
