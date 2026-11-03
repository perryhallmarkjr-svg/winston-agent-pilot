import unittest
from datetime import date

from listing_tools import folder_name, package_price, shoot_label


class ListingToolsTests(unittest.TestCase):
    def test_package_price(self):
        self.assertEqual(package_price("photos"), 175)
        self.assertEqual(package_price("photos+drone", twilight=True), 370)
        with self.assertRaises(ValueError):
            package_price("aerial-only")

    def test_folder_name(self):
        self.assertEqual(folder_name("1204 Oak Hollow Dr., Austin TX"), "1204-oak-hollow-dr-austin-tx")

    def test_shoot_label_weekday_and_year(self):
        label = shoot_label(date(2026, 11, 4))
        self.assertTrue(label.startswith("Wed, Nov"))
        self.assertTrue(label.endswith("2026"))


if __name__ == "__main__":
    unittest.main()
