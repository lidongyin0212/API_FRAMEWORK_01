import unittest  # 导入unittest
import requests


class TestUserLogin(unittest.TestCase):
    url = 'http://115.28.108.130:5000/api/user/login/'

    def test_user_login_normal(self):
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('登录成功', res.text)  # 断言

    def test_user_login_password_wrong(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('用户名或密码错误', res.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别
