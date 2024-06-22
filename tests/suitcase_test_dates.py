import unittest
import TestDates as test_dates


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_dates))
unittest.TextTestRunner(verbosity=2).run(suite)