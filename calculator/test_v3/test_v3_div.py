from calculator.calculatorPackage.mycalculator import Count
from calculator.test_v3.test_v3 import MyTest

class TestDiv(MyTest):
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