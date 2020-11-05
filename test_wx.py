import requests


class TestDepartment:
    def setup_class(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "method": "get",
            "params": {
                "corpid": "wwc159253c6ba0ffca",
                "corpsecret": "fGSZI1Ncd8NgGzLDePB5efg06uTbCWo6R5kHgSuAmIs"
            }
        }
        rsp = requests.request(**data).json()
        self.access_token = rsp['access_token']

    def test_add_department(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}",
            "method": "post",
            "json": {
                "name": "test研发中心",
                "name_en": "test_dev",
                "parentid": 1,
                "order": 1,
                "id": 2
            }
        }
        rsp_code = requests.request(**data).status_code
        assert rsp_code == 200

    def test_update_department(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}",
            "method": "post",
            "json": {
                "id": 2,
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1
            }
        }
        rsp = requests.request(**data)
        assert rsp.status_code == 200

    def test_del_deparment(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={2}",
            "method": "get"
        }
        rsp = requests.request(**data)
        assert rsp.status_code == 200

    def test_select_deparment(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}&id=1",
            "method": "get"
        }
        rsp = requests.request(**data)
        assert rsp.status_code == 200
