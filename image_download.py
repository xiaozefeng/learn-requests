#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def download_image():
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    response = requests.get('http://img5.imgtn.bdimg.com/it/u=2618612825,2054253508&fm=27&gp=0.jpg',headers = headers,stream=True)
    with open('demo.jpg','wb') as f:
        for chunk in response.iter_content(128):
            f.write(chunk)


def download_image_improved():
    # 伪造header信息
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    url = 'http://img5.imgtn.bdimg.com/it/u=2618612825,2054253508&fm=27&gp=0.jpg'
    # response = requests.get(url,headers = headers,stream =True)
    from contextlib import closing
    # 关闭打开的流
    with closing(requests.get(url, headers=headers,stream=True)) as response:
        with open('demo1.jpg','wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


# download_image()
download_image_improved()

