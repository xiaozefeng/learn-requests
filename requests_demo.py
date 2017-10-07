# coding:utf-8

import requests

IP_URL = 'http://127.0.0.1:8000/ip'
PARAM_URL= 'http://127.0.0.1:8000/get'

def use_simple_requests():
    response = requests.get(IP_URL)
    print(response.headers)
    print(response.text)


def use_params_requests():
    params = {'param1':'hello','param2':'world'}
    response  = requests.get(PARAM_URL,params=params)
    print('headers:',response.headers)
    print('status_code: ',response.status_code)
    print('json:',response.json())


use_simple_requests()
use_params_requests()
