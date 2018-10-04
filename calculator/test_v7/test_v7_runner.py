import unittest
from calculator.test_v7.test_v7_casesFind import casesSuite
from calculator.HTMLreport import HTMLTestRunner
import time

if __name__=="__main__":
    curTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename="CalFunTestReport"+curTime+".html"
    fp=open('E:/Python/demo/calculatorProject/report/'+filename, 'wb')

    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My Calculator Function Unit Test Report',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    suite = unittest.TestSuite()
    suite.addTests(casesSuite)
    runner.run(suite)
