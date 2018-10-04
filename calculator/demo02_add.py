#将每个功能测试编写成单独的类
#测试add函数

from calculator.calcu import Count
import unittest
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def test_add1(self):
        print("测试两个整数函数")
        c1=Count(10,20)
        res1=c1.add()
        print("计算实际结果：",res1)
        self.assertEqual(res1,30)

    def test_add2(self):
        print("测试两个浮点型数据函数")
        c2=Count(2167.45,3978.78)
        res2=c2.add()
        print("计算实际结果：",res2)
        if abs(res2-6146.23)<0.001:
            res2=6146.23
        self.assertEqual(res2,6146.23)

    def test_add3(self):
        print("测试两个字符串函数")
        c3=Count("你好","测试")
        res3=c3.add()
        print("实际计算结果：",res3)
        self.assertEqual(res3,"你好测试")

    def tearDown(self):
        print("测试结束\n")

if __name__=="__main__":
    suite=unittest.TestSuite()
    case_add1=TestAdd("test_add1")
    case_add2=TestAdd("test_add2")
    case_add3=TestAdd("test_add3")
    suite.addTest(case_add1)
    suite.addTest(case_add2)
    suite.addTest(case_add3)

    runner=unittest.TextTestRunner
    runner.run(suite)
