import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
import os

from src.dates import breakdown_date




class TestDates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df_in = pd.read_csv(os.path.join("data", "tests", "month_breakdown_input.csv"))
        cls._df_out = pd.read_csv(os.path.join("data", "tests", "month_breakdown_output.csv"))

    def test_breakdown_date(self):
        print("Starting breakdown_date")
        result_df = breakdown_date(self._df_in)
        assert_frame_equal(result_df, self._df_out)
        #self.assertTrue(breakdown_date(self._df_in) == self._df_out)
        