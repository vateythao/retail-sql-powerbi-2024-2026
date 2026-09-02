import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Clean_Data" / "sales_2024_2026_combined.csv"


class TestSalesData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(DATA_FILE)
        cls.df["SalesDate"] = pd.to_datetime(cls.df["SalesDate"])

    def test_expected_row_count(self):
        self.assertEqual(len(self.df), 9864)

    def test_no_missing_values(self):
        self.assertEqual(self.df.isnull().sum().sum(), 0)

    def test_no_duplicate_metric_dates(self):
        duplicate_count = self.df.duplicated(
            subset=["Metric", "SalesDate"]
        ).sum()

        self.assertEqual(duplicate_count, 0)

    def test_expected_columns(self):
        expected_columns = {"Metric", "SalesDate", "Amount"}

        self.assertTrue(
            expected_columns.issubset(self.df.columns)
        )

    def test_date_range(self):
        self.assertEqual(
            self.df["SalesDate"].min(),
            pd.Timestamp("2024-01-01")
        )

        self.assertEqual(
            self.df["SalesDate"].max(),
            pd.Timestamp("2026-12-31")
        )


if __name__ == "__main__":
    unittest.main()