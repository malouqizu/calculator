#使用普通方法对Count类进行测试
#此文件只对add函数进行浮点数加测试

from calculator.calcu import Count

mytest=Count(10.56,23.43)
res2=mytest.add()
if abs(res2-33.99)<=0.001:
    print("计算正确！")
else:
    print("计算错误！")
print("计算实际结果:",res2)
