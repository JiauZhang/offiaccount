from base.api import BaseAPI

class Draft(BaseAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'https://api.weixin.qq.com/cgi-bin/draft'

    def add(self, data):
        add_url = self.base_url + '/add?access_token=' + self.access_token
        pass

    def get(self, media_id):
        get_url = self.base_url + '/get?access_token=' + self.access_token
        pass

    def batchget(self, offset=0, count=20, no_content=0):
        # https://developers.weixin.qq.com/doc/offiaccount/Draft_Box/Get_draft_list.html
        batchget_url = self.base_url + '/batchget?access_token=' + self.access_token
        data = {
            'offset': offset,
            'count': count,
            'no_content': no_content,
        }
        self.post(url=batchget_url, data=data)

    def count(self):
        count_url = self.base_url + '/count?access_token=' + self.access_token
        return self.get(count_url)
