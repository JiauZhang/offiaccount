import requests
import json

class BaseAPI:
    def __init__(self, access_token=None, token_required=True):
        if token_required and access_token is None:
            raise RuntimeError('access_token is required, but access_token is None!')
        self.access_token = access_token

    def get(self, url=None, data={}):
        if url is None:
            raise RuntimeError('BaseAPI.get parameter of url is None!')

        jdata = json.dumps(data)
        r = requests.get(url=url, data=jdata)
        return r.json()

    def post(self, url, data={}):
        if url is None:
            raise RuntimeError('BaseAPI.post parameter of url is None!')

        # https://developers.weixin.qq.com/community/develop/doc/000024b3058f40fa792e40b2656000?highLine=draft%2520html
        jdata = json.dumps(data, ensure_ascii=False)
        latin1 = jdata.encode("utf-8").decode('latin1')
        r = requests.post(url=url, data=latin1)
        return r.json()
