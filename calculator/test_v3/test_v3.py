# 将每个测试类都需要的公共功能分离出来定义成一个新类

import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

