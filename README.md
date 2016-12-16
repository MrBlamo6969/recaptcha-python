# recaptcha-python
reCaptcha for python and Django
###Requirements
1. Python 2.7
2. requests 
```sh
$ pip install requests
```

| method    |parameters|return|  
|:---:|:---:|:---:|
|is_succes(data)| data  = 'g-recaptcha-response' | None or the value of the response|
|get_error_codes()| None |None or the errors for the last request (is_succes())|
|get_hostname()| None | None or the hostname for the last request (is_succes())|
|get_challenge_ts()|None |  None or the timestamp for the last request (is_succes())|
|reCaptchaDjango.sitekey()| None | the value of the site key (only works with Django module)|

###how to use ?
```py
from reCaptcha import reCaptcha
captcha = reCaptcha(secretKey= 'Your Secret Key')

# you need the post requests response with the data 
# supose that the response come in POST

data = POST['g-recaptcha-response']
value = captcha.is_succes(data)
```
###how to use with Django?
first add the following configuration to the configuration file:  
in settings.py

RECAPTCHA_SECRET_KEY = 'Your secret key'  
RECAPTCHA_SITE_KEY= 'Your site key'


```py

from django.http import JsonResponse, Http404
reCaptcha.reCaptchaDjango import challenge

# In the view that you want

@challenge(Http404)
def your_view(request):
    #raise Http404 if the challenge failed  Or not sent by POST
    pass
    
@challenge(JsonRespnse)
def your_view(request):
    #return default JsonResonse if the challenge failed  Or not sent by POST
    pass
    
@challenge(JsonRespnse({'create_your':'response'}))
def your_view(request):
    #return default JsonResonse if the challenge failed  Or not sent by POST
    pass
        
```