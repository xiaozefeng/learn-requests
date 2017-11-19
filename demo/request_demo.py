# coding: utf-8

import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET= 'http://127.0.0.1:8000/get'

def use_simple_requests():
    res = requests.get(URL_IP)
    print 'headers >>>>'
    print res.headers
    print 'body >>>>'
    print res.text
    
def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    # 发送请求
    res = requests.get(URL_GET, params=params)
    print 'headers >>>>'
    print res.headers
    print 'status code >>>>'
    print res.status_code, res.reason
    print 'body >>>>'
    print res.text 
    # res.json() 转换成json对象

if __name__ == '__main__':  
    print 'use simple requests'
    use_simple_requests()
    print 'use params requests'
    use_params_requests()
    
