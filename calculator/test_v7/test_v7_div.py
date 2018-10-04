import unittest
from calculator.test_v7.test_v7 import MyTest
from calculator.test_v7.test_v7_testData import GetTestData
from calculator.calculatorPackage.mycalculator import Count

class TestDiv(MyTest):
    def test_div1(self):
        print("使用多组数据测试两个整数div1")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile("E:/Python/demo/csv/importData/zhengshuData.csv")
        zhengshuData = getdata.getData(file)

        i = 0
        for x, y in zip(zhengshuData[1], zhengshuData[0]):
            d1 = Count(int(x), int(y))
            zhengshuData[2][i] = d1.div()
            print("计算实际结果：", zhengshuData[2][i])
            i = i + 1

        i = 0
        for item in zhengshuData[6]:
            zhengshuData[6][i] = float(item)
            i = i + 1

        for res, res_right in zip(zhengshuData[2], zhengshuData[6]):
            self.assertEqual(res, res_right)

    def test_div2(self):
        print("使用多组数据测试两个浮点型数据div2")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile('E:/Python/demo/csv/importData/fudianshuData.csv')
        fudianshuData = getdata.getData(file)

        i = 0
        for x, y in zip(fudianshuData[1], fudianshuData[0]):
            d2 = Count(float(x), float(y))
            fudianshuData[2][i] = d2.div()
            print("计算实际结果：", fudianshuData[2][i])
            i = i + 1

        i = 0
        for item in fudianshuData[6]:
            fudianshuData[6][i] = float(item)
            i = i + 1

        for res, res_right in zip(fudianshuData[2], fudianshuData[6]):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res, res_right)

if __name__=="__main__":
    Suite = unittest.TestSuite()
    divCases = unittest.TestLoader().loadTestsFromTestCase(TestDiv)
    Suite.addTests(divCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)


    '''
    Suite=unittest.TestSuite()
    case_div1=TestDiv("test_div1")
    case_div2=TestDiv("test_div2")
    Suite.addTest(case_div1)
    Suite.addTest(case_div2)

    runner=unittest.TextTestRunner()
    runner.run(Suite)
    '''

'''
list1_zhengshu=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
list2_zhengshu=[10,20,30,40,50,60,70,80,90,100]
res_zhengshuRight=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]
list2_fudianshu=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshuRight=[101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
