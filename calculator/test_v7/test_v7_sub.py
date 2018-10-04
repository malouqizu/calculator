#测试sub函数
import unittest
from calculator.test_v7.test_v7 import MyTest
from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v7.test_v7_testData import GetTestData

class TestSub(MyTest):
    def test_sub1(self):
        print("使用多组数据测试两个浮点型数据函数sub1")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile("E:/Python/demo/csv/importData/zhengshuData.csv")
        zhengshuData = getdata.getData(file)

        i = 0
        for x, y in zip(zhengshuData[1], zhengshuData[0]):
            s1 = Count(int(x), int(y))
            zhengshuData[2][i] = str(s1.sub())
            print("计算实际结果：", zhengshuData[2][i])
            i = i + 1

        for res, res_right in zip(zhengshuData[2], zhengshuData[4]):
            self.assertEqual(res, res_right)

    def test_sub2(self):
        print("使用多组数据测试两个浮点型数据函数sub2")
        print("开始获取测试数据：")
        getdata = GetTestData()
        file = getdata.openDataFile('E:/Python/demo/csv/importData/fudianshuData.csv')
        fudianshuData = getdata.getData(file)

        i = 0
        for x, y in zip(fudianshuData[1], fudianshuData[0]):
            s2 = Count(float(x), float(y))
            fudianshuData[2][i] = s2.sub()
            print("计算实际结果：", fudianshuData[2][i])
            i = i + 1

        i = 0
        for item in fudianshuData[4]:
            fudianshuData[4][i] = float(item)
            i = i + 1

        for res, res_right in zip(fudianshuData[2], fudianshuData[4]):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res, res_right)

if __name__=="__main__":
    Suite = unittest.TestSuite()
    subCases = unittest.TestLoader().loadTestsFromTestCase(TestSub)
    Suite.addTests(subCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)


    '''
    Suite=unittest.TestSuite()
    case_sub1=TestSub("test_sub1")
    case_sub2=TestSub("test_sub2")
    Suite.addTest(case_sub1)
    Suite.addTest(case_sub2)

    runner=unittest.TextTestRunner()
    runner.run(Suite)
    '''

'''
#测试数据
list1_zhengshu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2_zhengshu=[10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
res_zhengshuRight=[10,20,30,40,50,60,70,80,90,100]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  1.1,  2.1,  3.1,  4.1,  5.1,  6.1,  7.1,  8.1,  9.1]
list2_fudianshu=[10.2, 21.2, 32.2, 43.2, 54.2, 65.2, 76.2, 87.2, 98.2, 109.2]
res_fudianshuRight=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
