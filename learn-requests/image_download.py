# coding: utf-8

import requests

def download_image():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
    url = "http://img.mmjpg.com/small/2017/1171.jpg"
    res = requests.get(url, headers=headers, stream=True)
    with open('mm.jpg', 'wb') as f:
        for chunk in res.iter_content(128):
            f.write(chunk)


def download_image_improved():
    ''' 使用管理上下文的方式下载图片
    '''
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
    url = "http://img.mmjpg.com/small/2017/1171.jpg"
    from  contextlib import closing
    with closing(requests.get(url, headers=headers,stream=True)) as res:
        with open('mm1.jpg', 'wb') as f:
            for chunk in res.iter_content(128):
                f.write(chunk)

    
if __name__ =='__main__':
    # download_image()
    download_image_improved()
