# -*- coding: utf-8 -*-

import requests


def get_key_info(response,*args,**kw):
    print(response.headers['Content-Type'])


def main():
    requests.get('https://api.github.com',hooks=dict(response=get_key_info))



main()
