#测试sub函数

from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v5.test_v5 import MyTest
import unittest

#测试数据
list1_zhengshu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2_zhengshu=[10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
res_zhengshuRight=[10,20,30,40,50,60,70,80,90,100]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  1.1,  2.1,  3.1,  4.1,  5.1,  6.1,  7.1,  8.1,  9.1]
list2_fudianshu=[10.2, 21.2, 32.2, 43.2, 54.2, 65.2, 76.2, 87.2, 98.2, 109.2]
res_fudianshuRight=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class TestSub(MyTest):
    def test_sub1(self):
        print("使用多组数据测试两个整数函数sub")
        i=0
        for x,y in zip(list1_zhengshu,list2_zhengshu):
            s1=Count(y,x)
            res_zhengshu[i]=s1.sub()
            print("计算实际结果：",res_zhengshu[i])
            i=i+1
        for res, res_right in zip(res_zhengshu,res_zhengshuRight):
            self.assertEqual(res,res_right)

    def test_add2(self):
        print("使用多组数据测试两个浮点型数据函数sub")
        i=0
        for x,y in zip(list1_fudianshu,list2_fudianshu):
            s2=Count(y,x)
            res_fudianshu[i]=s2.sub()
            print("计算实际结果：",res_fudianshu[i])
            i=i+1

        for res, res_right in zip(res_fudianshu,res_fudianshuRight):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res,res_right)

if __name__=="__main__":
    '''
    Suite=unittest.TestSuite()
    case_sub1=TestSub("test_sub1")
    case_sub2=TestSub("test_sub2")
    Suite.addTest(case_sub1)
    Suite.addTest(case_sub2)

    runner=unittest.TextTestRunner()
    runner.run(Suite)
    '''
    Suite = unittest.TestSuite()
    subCases = unittest.TestLoader().loadTestsFromTestCase(TestSub)
    Suite.addTests(subCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)
