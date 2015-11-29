#!/usr/bin/python
""" Python Testing using python unittest library to test the
	initialization, rising, dropping, and fluctuating of stocks
"""

import unittest
import sys
sys.path.insert(0, '..')
from main import fluctuate
from main import rise
from main import drop
from main import Stock

class Test(unittest.TestCase):
	''' Main class for add testing; Can be added to a suite'''

	def setUp(self):
		"""The function "setUp" will always be ran in order to setup the
			test environment before all the tests have run.
		"""
		print ""
		"""Verify environment is setup properly""" ## Printed if test fails
		pass


	def tearDown(self):
		"""The function "tearDown" will always be ran in order to cleanup the
			test environment after all the tests have run.
		"""
		print ""
		"""Verify environment is tore down properly""" ## Printed if test fails
		pass

	def test_init(self):
		"""Testing the Initialization of a Stock Value"""
		stk = Stock(None, None, None, None, None, None, None)
		print stk.StockPrice
		try:
			self.assertEqual(stk.StockPrice, 0.0)
		except ValueError:
			print 'Failed: Stock Initialization not equivalent to 0.0'

	def test_rise(self):
		"""Testing the Implementation of a Stock Value Rising
			The funtion test_rise checks the original stock price to
			new raised stock price if it is incresed it passes otherwise fail.
		"""
		stk = Stock(None, None, None, None, None, None, None)
		stk.StockPrice = 120
		orig_stk_value = stk.StockPrice
		rise(stk)
		print 'Testing: ' + str(stk.StockPrice) + ' > ' + str(orig_stk_value)
		self.assertGreater(stk.StockPrice, orig_stk_value)

	def test_drop(self):
		"""Testing the Implementation of a Stock Value Dropping
			The funtion test_drop checks the original stock price to
			new raised stock price if it is incresed it passes otherwise fail.
		"""
		stk = Stock(None, None, None, None, None, None, None)
		stk.StockPrice = 120
		orig_stk_value = stk.StockPrice
		drop(stk)
		print 'Testing: ' + str(stk.StockPrice) + ' < ' + str(orig_stk_value)
		self.assertLess(stk.StockPrice, orig_stk_value)

	def test_fluctuate(self):
		"""Testing the Implementation of a Stock Value Fluctuating
			The function test_fluctuate implements a change in the stock value
			by either rising, dropping, or even remaining consistent.
		"""
		stk = Stock(None, None, None, None, None, None, None)
		stk.StockPrice = 120
		orig_stk_value = stk.StockPrice
		for x in xrange(1,70):
			#orig_stk_value = stk.StockPrice can't have or else if it goes in prime or other it does actually test correctly
			fluctuate(stk)
		self.assertNotEqual(stk.StockPrice, orig_stk_value)

if __name__=='__main__':
    unittest.main()
