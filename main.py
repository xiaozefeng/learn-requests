# coding:utf-8

import json
import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_uri('users/xiaozefeng'))
    print(better_print(response.text))


def get_emails():
    response = requests.get(build_uri('user/emails'),auth=('xiaozefeng','857269425xx'))
    print(better_print(response.text))


def hard_request():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET',build_uri('user/emails'), auth=('xiaozefeng','857269425xx'),headers =headers)
    prepped = req.prepare()
    print prepped.headers

    response = s.send(prepped,timeout=5)
    print response.status_code
    print better_print(response.text)

if __name__ =='__main__':
    #request_method()
    #get_emails()
    hard_request()

