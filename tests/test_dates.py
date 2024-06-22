import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
import os


from src.dates import breakdown_date, erase_month, format_date




class TestDates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df_in = pd.read_csv(os.path.join("data", "tests", "month_breakdown_input.csv"))
        cls._df_out = pd.read_csv(os.path.join("data", "tests", "month_breakdown_output.csv"))

    def test_breakdown_date(self):
        print("Starting breakdown_date")
        result_df = breakdown_date(self._df_in, test_mode=True)
        assert_frame_equal(result_df, self._df_out)
        #self.assertTrue(breakdown_date(self._df_in) == self._df_out)
        

    def test_erase_month(self):
        print("Starting erase_month")
        result_df = erase_month(self._df_in, test_mode=True)
        # Verify that month is not in the result columns
        self.assertNotIn("month", result_df.columns)  

        

class TestFormatDate(unittest.TestCase):
    
    # Verify that the result is a list
    def test_format_date_returns_list(self):
        result = format_date("2024-06")
        self.assertIsInstance(result, list)

    # Verify that the list has 2 elements
    def test_format_date_has_two_elements(self):
        result = format_date("2024-06")
        self.assertEqual(len(result), 2)

    # Verify that the first item has len = 4 (YYYY)
    def test_format_date_first_element_is_four_digit_year(self):
        result = format_date("2024-06")
        self.assertEqual(len(result[0]), 4)

    # Verify that the second item has len = 2 (MM)
    def test_format_date_second_element_is_two_digit_month(self):
        result = format_date("2024-06")
        self.assertEqual(len(result[1]), 2)

    def test_format_date_with_different_format(self):
        result = format_date("20234-05")
        self.assertEqual(result[0], "20234")
        self.assertEqual(result[1], "05")
