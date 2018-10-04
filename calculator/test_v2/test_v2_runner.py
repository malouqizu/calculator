import unittest
from calculator.test_v2.test_v2_add import TestAdd
from calculator.test_v2.test_v2_sub import TestSub
from calculator.test_v2.test_v2_div import TestDiv
from calculator.test_v2.test_v2_mul import TestMul

if __name__=="__main__":
    suite=unittest.TestSuite()

    case_add1=TestAdd("test_add1")
    case_add2=TestAdd("test_add2")
    case_add3=TestAdd("test_add3")
    suite.addTest(case_add1)
    suite.addTest(case_add2)
    suite.addTest(case_add3)

    case_sub1=TestSub("test_sub1")
    case_sub2 = TestSub("test_sub2")
    suite.addTest(case_sub1)
    suite.addTest(case_sub2)

    case_mul1 = TestMul("test_mul1")
    case_mul2 = TestMul("test_mul2")
    suite.addTest(case_mul1)
    suite.addTest(case_mul2)
    case_div1 = TestDiv("test_div1")
    case_div2 = TestDiv("test_div2")
    suite.addTest(case_div1)
    suite.addTest(case_div2)

    runner=unittest.TextTestRunner()
    runner.run(suite)
