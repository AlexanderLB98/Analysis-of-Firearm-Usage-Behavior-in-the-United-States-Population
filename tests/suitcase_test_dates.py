import unittest

import sys
import os
# Add root path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from test_dates import TestDates, TestFormatDate

def run_date_tests(ask=True):
    
    if ask:
        print("Select which suite you want to execute from date_tests:")
        print("0. All")
        print("1. TestDates")
        print("2. TestFormatDate")
        
        choice = input("Select: ")
        
        loader = unittest.TestLoader()
        
        
        if choice == "0":
            # Run all test cases
            suite = loader.loadTestsFromModule(sys.modules[__name__])
        elif choice == "1":
            suite = loader.loadTestsFromTestCase(TestDates)
        elif choice == "2":
            suite = loader.loadTestsFromTestCase(TestFormatDate)
            
    else:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])

    unittest.TextTestRunner(verbosity=2).run(suite)
    
if __name__ == '__main__':
    run_date_tests()