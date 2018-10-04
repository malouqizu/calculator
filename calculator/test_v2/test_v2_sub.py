#将每个功能测试编写成单独的类
#测试add函数

from calculator.calculatorPackage.mycalculator import Count
import unittest

#测试sub函数
class TestSub(unittest.TestCase):
    def setUp(self):
        print("测试sub函数")
    def test_sub1(self):
        print("测试整数sub")
        m1=Count(100,20)
        res1=m1.sub()
        print("实际计算结果：",res1)
        self.assertEqual(res1,80)
    def test_sub2(self):
        print("测试浮点数sub")
        m2=Count(4589.87,3978.78)
        res2=m2.sub()
        print("实际计算结果：",res2)
        if abs(res2-611.09)<0.01:
            res2=611.09
        self.assertEqual(res2,611.09)

    def tearDown(self):
        print("测试sub结束")

if __name__=="__main__":
    suite=unittest.TestSuite()
    case_sub1=TestSub("test_sub1")
    case_sub2 = TestSub("test_sub2")
    suite.addTest(case_sub1)
    suite.addTest(case_sub2)

    runner=unittest.TextTestRunner
    runner.run(suite)
