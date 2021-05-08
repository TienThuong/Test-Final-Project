from unittest import TestLoader, TestSuite

from HtmlTestRunner import HTMLTestRunner

from Test.test_contact import ContactUs
from Test.test_login import Login
from Test.test_order import Order
from Test.test_productdetail import Test_Product
from Test.test_search import Search

# Get all test from Test
test1 = TestLoader().loadTestsFromTestCase(ContactUs)
test2 = TestLoader().loadTestsFromTestCase(Login)

test3 = TestLoader().loadTestsFromTestCase(Order)
test4 = TestLoader().loadTestsFromTestCase(Test_Product)
test5 = TestLoader().loadTestsFromTestCase(Search)

# Creating test suites
# Sanity test suite
masterTestSuite = TestSuite([test1, test2, test3, test4, test5])
runner = HTMLTestRunner(output=r'..\\Reports', combine_reports=True, report_title="Final Report").run(masterTestSuite)
