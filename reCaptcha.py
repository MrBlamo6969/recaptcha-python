'''
    Created by : Cristian Steib
    date : 8/12/16
requiere 'requests'

para hacer uso de la api es impresindible primero instanciarla

ej :
  recap = reCaptcha()

lugo se solicita is_succes(param) y como paramtro se envia lo que recibe el post como 'g-recaptcha-response'


'''

import requests
import sys

class reCaptcha ():
    def __init__(self,secretKey):

        self.secretKey = secretKey
        self.url='https://www.google.com/recaptcha/api/siteverify'


    def __callApi(self, response):
        try:

            headers = {'User-Agent': 'DebuguearApi-Browser',}
            payload = {'secret': self.secretKey, 'response': response}
            r = requests.request(method='POST', url=self.url , headers=headers, data=payload)
            return r.json()

        except:
            print sys.exc_info()
            return False

    def is_succes(self,response):
        self.data = self.__callApi(response)
        if self.data:
            try:
                return self.data['success']
            except:
                return None
        else:
            return None

    def get_error_codes(self):
        #missing-input-secret	The secret parameter is missing.
        #invalid-input-secret	The secret parameter is invalid or malformed.
        #missing-input-response	The response parameter is missing.
        #invalid-input-response	The response parameter is invalid or malformed.
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
        #return time stamp
        try:
            return self.data['challenge_ts']
        except:
            return None



