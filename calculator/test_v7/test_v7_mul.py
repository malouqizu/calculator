import unittest
from calculator.test_v7.test_v7 import MyTest
from calculator.test_v7.test_v7_testData import GetTestData
from calculator.calculatorPackage.mycalculator import Count

class TestMul(MyTest):
    def test_mul1(self):
        print("使用多组数据测试两个整数mul1")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile("E:/Python/demo/csv/importData/zhengshuData.csv")
        zhengshuData = getdata.getData(file)

        i = 0
        for x, y in zip(zhengshuData[1], zhengshuData[0]):
            m1 = Count(int(x), int(y))
            zhengshuData[2][i] = m1.mul()
            print("计算实际结果：", zhengshuData[2][i])
            i = i + 1

        i = 0
        for item in zhengshuData[5]:
            zhengshuData[5][i] = float(item)
            i = i + 1

        for res, res_right in zip(zhengshuData[2], zhengshuData[5]):
            self.assertEqual(res, res_right)

    def test_mul2(self):
        print("使用多组数据测试两个浮点型数据mul2")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile('E:/Python/demo/csv/importData/fudianshuData.csv')
        fudianshuData = getdata.getData(file)

        i = 0
        for x, y in zip(fudianshuData[1], fudianshuData[0]):
            m2 = Count(float(x), float(y))
            fudianshuData[2][i] = m2.mul()
            print("计算实际结果：", fudianshuData[2][i])
            i = i + 1

        i = 0
        for item in fudianshuData[5]:
            fudianshuData[5][i] = float(item)
            i = i + 1

        for res, res_right in zip(fudianshuData[2], fudianshuData[5]):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res, res_right)


if __name__=="__main__":
    Suite = unittest.TestSuite()
    mulCases = unittest.TestLoader().loadTestsFromTestCase(TestMul)
    Suite.addTests(mulCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)

'''
Suite=unittest.TestSuite()
case_mul1=TestMul("test_mul1")
case_mul2=TestMul("test_mul2")
Suite.addTest(case_mul1)
Suite.addTest(case_mul2)

runner=unittest.TextTestRunner()
runner.run(Suite)
'''
'''
list1_zhengshu=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
list2_zhengshu=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
res_zhengshuRight=[10,20,30,40,50,60,70,80,90,100]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]
list2_fudianshu=[101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]
res_fudianshuRight=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

