import unittest
from calculator.test_v6.test_v6_add import TestAdd
from calculator.test_v6.test_v6_sub import TestSub
from calculator.test_v6.test_v6_div import TestDiv
from calculator.test_v6.test_v6_mul import TestMul

addCases=unittest.TestLoader().loadTestsFromTestCase(TestAdd)
subCases=unittest.TestLoader().loadTestsFromTestCase(TestSub)
divCases=unittest.TestLoader().loadTestsFromTestCase(TestDiv)
mulCases=unittest.TestLoader().loadTestsFromTestCase(TestMul)

casesSuite=[addCases,subCases,divCases,mulCases]

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTests(casesSuite)

    runner=unittest.TextTestRunner()
    runner.run(suite)