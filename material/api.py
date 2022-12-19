from base.api import BaseAPI

class Material(BaseAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'https://api.weixin.qq.com/cgi-bin/material'

    def add(self, data):
        # https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Adding_Permanent_Assets.html
        add_url = self.base_url + '/add?access_token=' + self.access_token
        return self.post(url=add_url, data=data)

    def get(self, media_id):
        get_url = self.base_url + '/get?access_token=' + self.access_token
        pass

    def batchget(self, type, offset=0, count=20):
        # https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_materials_list.html
        _type_allow_list = ['image', 'video', 'voice', 'news']
        if type not in _type_allow_list:
            raise RuntimeError('Material.batchget type must be set in', _type_allow_list)

        batchget_url = self.base_url + '/batchget_material?access_token=' + self.access_token
        data = {
            'type': type,
            'offset': offset,
            'count': count,
        }
        return self.post(url=batchget_url, data=data)

    def count(self):
        # https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_the_total_of_all_materials.html
        count_url = self.base_url + '/get_materialcount?access_token=' + self.access_token
        return self.get(count_url)
