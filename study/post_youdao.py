import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15887448534084'


def get_sign():
    return '2d92614b6687aa594237b0b8dd565f5c'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
           #"1588751821873"

form_data={
    'i': '我和你都是中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '6b71bda0785160f59caa738e5cbcdf96',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)