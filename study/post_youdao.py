import random
import requests
import time

#url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#content="我和你"

class   Youdao():
    def __index__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
        # print("random = ",s)
        # print("ts= ",t)
  #     print("salt=",t+s)
        return t+s
     #  return '15887448534084'

    def get_md5(self,value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
 #   print("s=",s," md5=",get_md5(s))
        return self.get_md5(s)
   # return '2d92614b6687aa594237b0b8dd565f5c'


    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        return ts
           #"1588751821873"


  #  def get_content(self):
    #    return content

    def yield_form_data(self):
        form_data={
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '6b71bda0785160f59caa738e5cbcdf96',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data


    def get_headers(self):
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1350908251@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=947082420.5523819; _ntes_nnid=318c45b2e2e4328898aa554fb3126e8d,1583464702862; P_INFO=wlk18768253391; JSESSIONID=aaavHTdB-c3Jk8hlDGOhx; ___rl__test__cookies=1588751821854',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        return headers


    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__name__':
   youdao=Youdao('我们')
   print(youdao.fanyi())