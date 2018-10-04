from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v4.test_v4 import MyTest

class TestMul(MyTest):
    def test_mul1(self):
        print("测试两个整数mul")
        m1=Count(10,20)
        res1=m1.mul()
        print("实际计算结果:",res1)
        self.assertEqual(res1,200)

    def test_mul2(self):
        print("测试两个浮点型数据mul")
        m2 = Count(20.45, 45.67)
        res2 = m2.mul()
        print("实际计算结果:", res2)
        if abs(res2-933.9515)<0.01:
            res2=933.9515
        self.assertEqual(res2, 933.9515)
import unittest
from calculator.demo04_caseFind import casesSuite

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTests(casesSuite)

    runner=unittest.TextTestRunner()
    runner.run(suite)
