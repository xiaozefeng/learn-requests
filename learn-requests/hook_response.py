# coding: utf-8

import requests

def get_key_info(res, *args, **kw):
    print res.headers['Content-Type']
    print args
    print kw

def main():
    ''' 自动调用钩子函数
    '''
    requests.get('https://api.github.com', hooks=dict(response=get_key_info))


if __name__ == '__main__':
    main()

