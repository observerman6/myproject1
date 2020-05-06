import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i': '我和你都是中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15887448534084',
    'sign': '2d92614b6687aa594237b0b8dd565f5c',
    'ts': '1588744853408',
    'bv': '6b71bda0785160f59caa738e5cbcdf96',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)