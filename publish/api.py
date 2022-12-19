from base.api import BaseAPI

class Publish(BaseAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'https://api.weixin.qq.com/cgi-bin/freepublish'

    def batchget(self, offset=0, count=20, no_content=0):
        # https://developers.weixin.qq.com/doc/offiaccount/Publish/Get_publication_records.html
        batchget_url = self.base_url + '/batchget?access_token=' + self.access_token
        data = {
            'offset': offset,
            'count': count,
            'no_content': no_content,
        }
        return self.post(url=batchget_url, data=data)