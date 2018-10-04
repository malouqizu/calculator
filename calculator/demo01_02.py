#使用unittest测试框架，对calculator所有功能进行测试

from calculator.calcu import Count
#步骤1：导入unittest模块
import unittest
#步骤2：编写测试类TestCount，继承TestCase类
class TestCount(unittest.TestCase):
    #步骤3：重写setUp函数
    def setUp(self):
        print("测试开始")
    #步骤4：编写测试函数test_add1()
    def test_add1(self):
        print("测试两个整数函数")
        c1=Count(10,20)
        res1=c1.add()
        print("计算实际结果：",res1)
    #步骤5：使用unittest提供的断言函数
        self.assertEqual(res1,30)

    #测试两个浮点型数据
    def test_add2(self):
        print("测试两个浮点型数据函数")
        c2=Count(2167.45,3978.78)
        res2=c2.add()
        print("计算实际结果：",res2)
        if abs(res2-6146.23)<0.001:
            res2=6146.23
        self.assertEqual(res2,6146.23)

    #测试两个字符串函数
    def test_add3(self):
        print("测试两个字符串函数")
        c3=Count("你好","测试")
        res3=c3.add()
        print("实际计算结果：",res3)
        self.assertEqual(res3,"你好测试")

    def test_sub1(self):
        print("测试整数sub")
        s1=Count(100,20)
        res1=s1.sub()
        print("实际计算结果：",res1)
        self.assertEqual(res1,80)

    def test_sub2(self):
        print("测试浮点数sub")
        s2=Count(4589.87,3978.78)
        res2=s2.sub()
        print("实际计算结果：",res2)
        if abs(res2-611.09)<0.01:
            res2=611.09
        self.assertEqual(res2,611.09)

    def test_div1(self):
        print("测试两个整数div")
        d1=Count(100,20)
        res1=d1.div()
        print("实际计算结果:",res1)
        self.assertEqual(res1,5)

    def test_div2(self):
        print("测试两个浮点型数据div")
        d2 = Count(245.45, 34.67)
        res2 = d2.div()
        print("实际计算结果:", res2)
        if abs(res2-7.0796)<0.01:
            res2=7.0796
        self.assertEqual(res2, 7.0796)

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

    #步骤6：重写tearDown函数
    def tearDown(self):
        print("测试结束\n")

if __name__=="__main__":
    #步骤7：将测试用例添加到测试套件
    suite=unittest.TestSuite()
    case1=TestCount("test_add1")
    case2=TestCount("test_add2")
    case3=TestCount("test_add3")
    case4=TestCount("test_sub1")
    case5=TestCount("test_sub2")
    case6=TestCount("test_div1")
    case7=TestCount("test_div2")
    case8=TestCount("test_mul1")
    case9=TestCount("test_mul2")
    suite.addTest(case1)
    suite.addTest(case2)
    suite.addTest(case3)
    suite.addTest(case4)
    suite.addTest(case5)
    suite.addTest(case6)
    suite.addTest(case7)
    suite.addTest(case8)
    suite.addTest(case9)

    #步骤8：执行测试套件
    runner=unittest.TextTestRunner
    runner.run(suite)


