# coding: utf-8

import urllib, urllib2

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET= 'http://127.0.0.1:8000/get'

def use_simple_urllib2():
    res = urllib2.urlopen(URL_IP)
    print 'headers >>>>'
    print res.info()
    print 'body >>>>'
    print ''.join([line for line in res.readlines()])

def use_params_urllib2():
    # 构建参数
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    print params
    # 发送请求
    res = urllib2.urlopen('?'.join([URL_GET,'%s']) % params)
    print 'headers >>>>'
    print res.info()
    print 'body >>>>'
    print ''.join([line for line in res.readlines()])

if __name__ == '__main__':  
    print 'use urllib2'
    # use_simple_urllib2()
    use_params_urllib2()
    