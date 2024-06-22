import unittest
import pandas as pd
#from pandas.testing import assert_frame_equal

#from src.dates import breakdown_date, erase_month, format_date
from src.common import clean_csv, rename_col


class TestCleanCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            "year": [2020, 2020, 2020, 2020, 2020],
            "month": [3, 3, 3, 3, 3],
            "state": ["Alabama", "Alaska", "Arizona", "Arkansas", "California"],
            "permit": [31205.0, 143.0, 5685.0, 2424.0, 27792.0],
            "handgun": [34897.0, 4657.0, 46377.0, 15304.0, 81543.0],
            "long_gun": [17850.0, 3819.0, 19346.0, 8968.0, 48616.0],
            "returned_to_seller_long_gun": [2, 3, 5, 6, 1],
            "returned_to_seller_hand_gun": [21, 2, 66, 23, 0]
        }
        cls.df_in = pd.DataFrame(data)

    def test_clean_csv_columns(self):
        # Verify the columns
        cleaned_df = clean_csv(self.df_in)
        expected_columns = ["month", "state", "permit", "handgun", "long_gun"]
        self.assertEqual(list(cleaned_df.columns), expected_columns)

    def test_clean_csv_month_type(self):
        # Verify the correct type for month
        cleaned_df = clean_csv(self.df_in)
        self.assertEqual(cleaned_df["month"].dtypes, int)

    def test_clean_csv_state_type(self):
        # Verificar que todos los elementos en la columna "state" sean str
        cleaned_df = clean_csv(self.df_in)
        self.assertTrue(cleaned_df["state"].apply(type).eq(str).all())

    def test_clean_csv_permit_type(self):
        # Verificar que todos los elementos en la columna "permit" sean int
        cleaned_df = clean_csv(self.df_in)
        self.assertEqual(cleaned_df["permit"].dtypes, int)

    def test_clean_csv_handgun_type(self):
        # Verificar que todos los elementos en la columna "permit" sean int
        cleaned_df = clean_csv(self.df_in)
        self.assertEqual(cleaned_df["handgun"].dtypes, int)

    def test_clean_csv_long_gun_type(self):
        # Verificar que todos los elementos en la columna "permit" sean int
        cleaned_df = clean_csv(self.df_in)
        self.assertEqual(cleaned_df["long_gun"].dtypes, int)


class TestRenameCol(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            "long_gun": [17850.0, 3819.0, 19346.0, 8968.0, 48616.0],
        }
        cls.df_in = pd.DataFrame(data)

    def test_rename_col_name(self):
        # Verify the column name
        cleaned_df = rename_col(self.df_in)
        expected_column_name = "longgun"
        self.assertIn(expected_column_name, cleaned_df.columns)

    