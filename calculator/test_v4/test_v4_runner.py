import unittest
from calculator.test_v4.test_v4_caseFind import casesSuite

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTests(casesSuite)

    runner=unittest.TextTestRunner()
    runner.run(suite)
