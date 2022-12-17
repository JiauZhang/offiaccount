from base.api import BaseAPI

class Tokenizer(BaseAPI):
    def __init__(self, appid, secret, **kwargs):
        super().__init__(**kwargs)

        self.appid = appid
        self.secret = secret
        self.token_url = \
            'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'\
            .format(self.appid, self.secret)
        self.json_key = 'access_token'

        ip_url = 'http://httpbin.org/ip'
        ip_info = self.get(url=ip_url)
        self.ip = ip_info['origin']

        self.update()

    def update(self):
        r = self.get(url=self.token_url)
        self.access_token = r[self.json_key]
