## Creating a test framework for rise function & drop function
#

""" This is a simple program to demonstrate how to create a unittest in
    Python. For more information and documentation, please see the official
    documentation page here: http://docs.python.org/library/unittest.html
"""

import unittest 
import main as a

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

	## The funtion "testRise" checks the original stock price to 
	# new raised stock price if it is incresed it passes otherwise fail.
	def testRise(self):
		#testStock

		testRiseInput = 990
		testRiseOutput = 990
		#testStock.value = testRiseInput
		#Rise(testStock);
		#testRiseOutput = testStock.value
		print "Testing Rise"
		try:
			self.assertGreater(testRiseOutput,testRiseInput)
		except:
			print "FAIL with input of "+testRiseInput+" and output: "+ testRiseOutput
		#print "a.main.price = %d" % a.rise.priceTemp
		pass

	## The funtion "testRise" checks the original stock price to 
	# new raised stock price if it is incresed it passes otherwise fail.
	def testDrop(self):
		print "Testing Drop"
		#self.assertGreaterEqual(rise(stk, stock_list)
		#print "a.main.price = %d" % a.rise.priceTemp
		pass


if __name__=='__main__':
    unittest.main()

    