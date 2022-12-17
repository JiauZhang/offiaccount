import requests
import json

class BaseAPI:
    def __init__(self, access_token=None):
        self.access_token = access_token

    def get(self, url=None, data={}):
        if url is None or self.access_token is None:
            raise RuntimeError('BaseAPI.get parameter of url is None!')

        jdata = json.dumps(data)
        r = requests.get(url=url, data=jdata)
        return r.json()

    def post(self, url, data={}):
        if url is None or self.access_token is None:
            raise RuntimeError('BaseAPI.post parameter of url is None!')

        jdata = json.dumps(data)
        r = requests.post(url=url, data=jdata)
        return r.json()
