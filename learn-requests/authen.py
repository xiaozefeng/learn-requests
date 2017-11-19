# coding: utf-8 

import requests
import json
import base64
from requests.auth import AuthBase

class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r ):
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r

BASE_URL= 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def basic_auth():
    '''
    基本认证
    '''
    res = requests.get(construct_url("user/emails") ,auth=('imoocdemo','imoocdemo123'), timeout=5)
    print res.status_code
    print better_print(res.text)
    print res.request.headers
    print base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw==')

def basic_oauth():
    '''
    7256af0cb9cb298e29a090800d05ba2cf326a07f
    oauth token 认证
    '''
    headers = {"Authorization": 'token 7256af0cb9cb298e29a090800d05ba2cf326a07f'}
    res = requests.get(construct_url("user/emails"), headers=headers)
    print res.status_code
    print better_print(res.text)
    print res.request.headers

def oauth_advanced():
    oauth = GithubAuth('7256af0cb9cb298e29a090800d05ba2cf326a07f')
    res = requests.get(construct_url("user/emails"), auth=oauth)
    print res.status_code
    print better_print(res.text)

if __name__ == '__main__':
    # basic_auth()
    # basic_oauth()
    oauth_advanced()
    