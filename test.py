## Creating a test framework for rise function & drop function
#

""" This is a simple program to demonstrate how to create a unittest in
    Python. For more information and documentation, please see the official
    documentation page here: http://docs.python.org/library/unittest.html
"""

import unittest
from main import rise
from main import drop
from main import Stock

## The following is the class in which all functions will be ran by unittest
#

class Test(unittest.TestCase):
	''' Main class for add testing; Can be added to a suite'''

	## The function "setUp" will always be ran in order to setup the
	# test environment before all the tests have run.
	def setUp(self):
		print ""
		"""Verify environment is setup properly""" ## Printed if test fails
		pass

	## The function "tearDown" will always be ran in order to cleanup the
	# test environment after all the tests have run.
	def tearDown(self):
		print ""
		"""Verify environment is tore down properly""" ## Printed if test fails
		pass

	def test_init(self):
		"""Testing the Initialization of a Stock Value"""
		print 'Testing the Initialization of a Stock Value'
		stk = Stock()
		print 'in the test_init'
		#stk.StockPrice = 1.5
		print stk.StockPrice
		print 'after the init'
		#self.assertEqual(stk.StockPrice, 0.0)
		try:
			self.assertEqual(stk.StockPrice, 0.0)
		except ValueError:
			print 'Failed: Stock Initialization not equivalent to 0.0'


	## The funtion "testRise" checks the original stock price to
	# new raised stock price if it is incresed it passes otherwise fail.
	def test_rise(self):
		"""Testing the Implementation of a Stock Value Rising"""
		stk = Stock()
		stk.StockPrice = 120
		orig_stk_value = stk.StockPrice
		rise(stk)
		print 'Testing: ' + str(stk.StockPrice) + ' > ' + str(orig_stk_value)
		self.assertGreater(stk.StockPrice, orig_stk_value)
		

	## The funtion "testRise" checks the original stock price to
	# new raised stock price if it is incresed it passes otherwise fail.
	def test_drop(self):
		"""Testing the Implementation of a Stock Value Dropping"""
		stk = Stock()
		stk.StockPrice = 120
		orig_stk_value = stk.StockPrice
		drop(stk)
		print 'Testing: ' + str(stk.StockPrice) + ' < ' + str(orig_stk_value)
		self.assertLess(stk.StockPrice, orig_stk_value)

	def test_fluctuate(self):
		stk = Stock()
		for x in xrange(1,70):
			fluctuate(stk)


if __name__=='__main__':
    unittest.main()
