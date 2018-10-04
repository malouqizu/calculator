#测试sub函数

from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v3.test_v3 import MyTest

class TestSub(MyTest):
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
