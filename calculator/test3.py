#使用普通方法对Count类进行测试
#此文件只对add函数进行字符串加测试

from calculator.calcu import Count

class TestCount:
    def test_add(self):
        c1=Count("你好","Python！")
        res1=c1.add()
        if res1=="你好Python！":
            print("计算正确！")
        else:
            print("计算错误！")
        print("计算实际结果：",res1)

mytest=TestCount()
mytest.test_add()