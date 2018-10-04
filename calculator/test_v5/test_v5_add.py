#test_v1到test_v4版本主要是搭建测试架构的一步步升级，力求使代码的框架比较清晰
#将测试代码与计算器实现代码分开，将计算器不同功能的测试代码放到不同模块当中
#从test_v5开始将实现测试所需数据与测试算法的分离，真正做到程序=算法+数据结构的哲学思想
#将数据放到单独数据结构中也可以实现每个功能模块进行多数据测试的目的

#test_v5初始版将数据直接存储在列表当中

#测试add函数
from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v5.test_v5 import MyTest
import unittest

#测试数据
list1_zhengshu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2_zhengshu=[10,20,30,40,50,60,70,80,90,100]
res_zhengshuRight=[10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_fudianshu=[0.1,  1.1,  2.1,  3.1,  4.1,  5.1,  6.1,  7.1,  8.1,  9.1]
list2_fudianshu=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshuRight=[10.2, 21.2, 32.2, 43.2, 54.2, 65.2, 76.2, 87.2, 98.2, 109.2]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list1_zifuchaun=["张三learn:", "李四learn:", "王五learn:", "小红study:", "小明study:"]
list2_zifuchaun=["Java!",        "C++!",        "Python!",    "Perl!",      "Shell!"]
res_zifuchaunRight=["张三learn:Java!", "李四learn:C++!", "王五learn:Python!",
                  "小红study:Perl!", "小明study:Shell!"]
res_zifuchaun=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class TestAdd(MyTest):
    def test_add1(self):
        print("使用多组数据测试两个整数函数")
        i=0
        for x,y in zip(list1_zhengshu,list2_zhengshu):
            a1=Count(x,y)
            res_zhengshu[i]=a1.add()
            print("计算实际结果：",res_zhengshu[i])
            i=i+1
        for res, res_right in zip(res_zhengshu,res_zhengshuRight):
            self.assertEqual(res,res_right)

    def test_add2(self):
        print("使用多组数据测试两个浮点型数据函数")
        i=0
        for x,y in zip(list1_fudianshu,list2_fudianshu):
            a2=Count(x,y)
            res_fudianshu[i]=a2.add()
            print("计算实际结果：",res_fudianshu[i])
            i=i+1

        for res, res_right in zip(res_fudianshu,res_fudianshuRight):
            if abs(res - res_right) < 0.001:
                res = res_right
            self.assertEqual(res,res_right)

    def test_add3(self):
        print("使用多组数据测试两个字符串函数")
        i=0
        for x,y in zip(list1_zifuchaun,list2_zifuchaun):
            a3=Count(x,y)
            res_zifuchaun[i]=a3.add()
            print("计算实际结果：",res_zifuchaun[i])
            i=i+1
        for res, res_right in zip(res_zifuchaun,res_zifuchaunRight):
            self.assertEqual(res,res_right)

if __name__=="__main__":
    '''
    Suite=unittest.TestSuite()
    case_add1=TestAdd("test_add1")
    Suite.addTest(case_add1)

    runner=unittest.TextTestRunner()
    runner.run(Suite)
    '''
    Suite = unittest.TestSuite()
    addCases = unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    Suite.addTests(addCases)

    runner = unittest.TextTestRunner()
    runner.run(Suite)
