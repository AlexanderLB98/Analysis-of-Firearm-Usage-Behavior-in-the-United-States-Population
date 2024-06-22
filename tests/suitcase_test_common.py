import unittest

import sys
import os
# Add root path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from test_common import TestCleanCSV, TestRenameCol




def run_common_tests(ask=True):
    
    if ask:
        print("Select which suite you want to execute:")
        print("0. All")
        print("1. TestCleanCSV")
        print("2. TestRenameCol")
        
        choice = input("Select: ")
        
        #suite = unittest.TestSuite() # Deprecated
        loader = unittest.TestLoader()
        
        
        if choice == "0":
            # Run all test cases
            suite = loader.loadTestsFromModule(sys.modules[__name__])
        elif choice == "1":
            suite = loader.loadTestsFromTestCase(TestCleanCSV)
        elif choice == "2":
            suite = loader.loadTestsFromTestCase(TestRenameCol)
    
    else:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
            
    unittest.TextTestRunner(verbosity=2).run(suite)
    
if __name__ == '__main__':
    run_common_tests()