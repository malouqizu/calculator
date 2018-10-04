from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v5.test_v5 import MyTest
import unittest

list1_zhengshu=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
list2_zhengshu=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
res_zhengshuRight=[10,20,30,40,50,60,70,80,90,100]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]
list2_fudianshu=[101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]
res_fudianshuRight=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class TestMul(MyTest):
    def test_mul1(self):
        print("使用多组数据测试两个整数mul")
        i = 0
        for x, y in zip(list1_zhengshu, list2_zhengshu):
            m1 = Count(x, y)
            res_zhengshu[i] = m1.mul()
            print("计算实际结果：", res_zhengshu[i])
            i = i + 1
        for res, res_right in zip(res_zhengshu, res_zhengshuRight):
            self.assertEqual(res, res_right)

    def test_mul2(self):
        print("使用多组数据测试两个浮点型数据mul")
        i = 0
        for x, y in zip(list1_fudianshu, list2_fudianshu):
            m2 = Count(x, y)
            res_fudianshu[i] = m2.mul()
            print("计算实际结果：", res_fudianshu[i])
            i = i + 1
        for res, res_right in zip(res_fudianshu, res_fudianshuRight):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res, res_right)

if __name__=="__main__":
    '''
    Suite=unittest.TestSuite()
    case_mul1=TestMul("test_mul1")
    case_mul2=TestMul("test_mul2")
    Suite.addTest(case_mul1)
    Suite.addTest(case_mul2)

    runner=unittest.TextTestRunner()
    runner.run(Suite)
    '''
    Suite = unittest.TestSuite()
    mulCases = unittest.TestLoader().loadTestsFromTestCase(TestMul)
    Suite.addTests(mulCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)
