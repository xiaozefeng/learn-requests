import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_url(endpoint):
    return '/'.join([URL, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    res = requests.get(build_url("users/imoocdemo"))
    print better_print(res.text)

def get_email():
    res = requests.get(build_url("user/emails"), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(res.text)

def params_request():
    res = requests.get(build_url("users"), params={'since': 11})
    print better_print(res.text)
    print res.request.headers
    print res.request.url

def json_request():
    # res = requests.patch(build_url("user"),auth=('imoocdemo', 'imoocdemo123'),json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'})
    res = requests.post(build_url('user/emails'), auth=('imoocdemo', 'imoocdemo123'),
    json=['hello-requests@163.com'])
    print better_print(res.text)
    print res.status_code

def timeout_request():
    try:
        res = requests.get(build_url("user/emails"), timeout=0.1)
        res.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e :
        print e.message

def hard_request():
    from requests import Session, Request
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_url("user/emails"), auth=("imoocdemo", 'imoocdemo123'), headers = headers)
    prepared = req.prepare()
    res = s.send(prepared, timeout=5)
    print res.status_code
    print better_print(res.text)
    print res.request.headers

if __name__ == '__main__':
    # request_method()
    # get_email()
    # params_request()
    # json_request()
    # timeout_request()
    hard_request()
