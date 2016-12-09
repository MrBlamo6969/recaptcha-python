'''
    Created by : Cristian Steib
    date : 8/12/16
    necesitas agregar en el setting de tu proyecto lo siguiente:

    RECAPTCHA_SECRET_KEY = ' tu clave '

'''
from django.conf import settings
from django.http import JsonResponse, Http404
import requests


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class reCaptcha():
    def __init__(self):

        self.secretKey = settings.RECAPTCHA_SECRET_KEY
        self.url = 'https://www.google.com/recaptcha/api/siteverify'

    def sitekey(self):
        try:

            return settings.RECAPTCHA_SITE_KEY

        except:
            return None

    def __callApi(self, response):
        try:

            headers = {'User-Agent': 'DebuguearApi-Browser', }
            payload = {'secret': self.secretKey, 'response': response}
            r = requests.request(method='POST', url=self.url, headers=headers, data=payload)
            return r.json()

        except:
            return False

    def is_succes(self, request):
        try:
            captchaResponse = request.POST['g-recaptcha-response']
        except:
            return False

        self.data = self.__callApi(captchaResponse)

        if self.data:
            try:
                return self.data['success']
            except:
                return None
        else:
            return None

    def get_error_codes(self):
        # missing-input-secret	The secret parameter is missing.
        # invalid-input-secret	The secret parameter is invalid or malformed.
        # missing-input-response	The response parameter is missing.
        # invalid-input-response	The response parameter is invalid or malformed.
        try:
            return self.data['error-codes']
        except:
            return None

    def get_hostname(self):
        try:
            return self.data['hostname']
        except:
            return None

    def get_challenge_ts(self):
        # return time stamp
        try:
            return self.data['challenge_ts']
        except:
            return None


def challenge(response):
    '''
    decorator just simple do from reCaptchaDjango import challenge
    then @challenge(Http404) or @challenge(JsonRespose)
    :param response:
    :return:
    '''

    def challenge_do(func):
        def check_captcha(*args, **kwargs):
            cap = reCaptcha()
            if cap.is_succes(*args):
                return func(*args, **kwargs)
            else:
                if (response == Http404):
                    raise Http404
                elif response == JsonResponse:
                    return response({'status': False,
                                     'error': 'bad captcha',
                                     'errorType': 150})
                else:
                    response

        return check_captcha

    return challenge_do
