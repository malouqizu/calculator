import unittest
from calculator.test_v6.test_v6_casesFind import casesSuite

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTests(casesSuite)

    runner=unittest.TextTestRunner()
    runner.run(suite)
