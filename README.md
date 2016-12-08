# recaptcha-python
reCaptcha for python and Django
###Requirements
1. Python 2.7
2. requests 
```sh
$ pip install requests
```
###how to use ?
```py
>>> from reCaptcha import reCaptcha
>>> captcha = reCaptcha(secretKey= 'Your Secret Key')

# you need the post requests response with the data 
# supose that the response come in POST

>>> data = POST['g-recaptcha-response']
>>> value = captcha.is_succes(data)
```