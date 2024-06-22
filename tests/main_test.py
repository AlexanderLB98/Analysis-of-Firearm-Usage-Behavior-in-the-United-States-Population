import unittest
import sys
import os

# Add root path (adjust the path as per your project structure)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from suitcase_test_common import run_common_tests
from suitcase_test_dates import run_date_tests

if __name__ == '__main__':
    print("Select which suite(s) you want to execute:")
    print("0. All suite cases")
    print("1. Common suite Tests")
    print("2. Date suite Tests")
    
    choice = input("Select: ")
    
    if choice == "0":
        run_common_tests(ask=False)
        run_date_tests(ask=False)
    elif choice == "1":
        run_common_tests()
    elif choice == "2":
        run_date_tests()
    else:
        print("Invalid choice. Running all suites by default.")
        run_common_tests()
        run_date_tests()
