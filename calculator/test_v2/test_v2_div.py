#将每个功能测试编写成单独的类
#测试div函数

from calculator.calculatorPackage.mycalculator import Count
import unittest

class TestDiv(unittest.TestCase):
    def setUp(self):
        print("测试div函数开始")

    def test_div1(self):
        print("测试两个整数div")
        c1=Count(100,20)
        res1=c1.div()
        print("实际计算结果:",res1)
        self.assertEqual(res1,5)

    def test_div2(self):
        print("测试两个浮点型数据div")
        c2 = Count(245.45, 34.67)
        res2 = c2.div()
        print("实际计算结果:", res2)
        if abs(res2-7.0796)<0.01:
            res2=7.0796
        self.assertEqual(res2, 7.0796)
    def tearDown(self):
        print("测试div结束\n")

if __name__=="__main__":
    suite=unittest.TestSuite()
    case_div1=TestDiv("test_div1")
    case_div2 = TestDiv("test_div2")
    suite.addTest(case_div1)
    suite.addTest(case_div2)
    runner=unittest.TextTestRunner()
    runner.run(suite)