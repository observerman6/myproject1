import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content="我和你"

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
   # print("random = ",s)
   # print("ts= ",t)
  #  print("salt=",t+s)
    return t+s
  #  return '15887448534084'


def get_sign():
    return '2d92614b6687aa594237b0b8dd565f5c'


def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
           #"1588751821873"



form_data={
    'i': 'get_content()',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': 'get_salt()',
    'sign': 'get_sign()',
    'ts': 'get_ts()',
    'bv': '6b71bda0785160f59caa738e5cbcdf96',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)