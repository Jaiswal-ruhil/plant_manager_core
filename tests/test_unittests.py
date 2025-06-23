import unittest

from system import Part
import pprint

class TestUnitTests(unittest.TestCase):
    def test_example(self):
        # Example test case
        self.assertEqual(1 + 1, 2) 

    def test_another_example(self):
        # Another example test case
        self.assertTrue(True)

    def test_part_creation(self):
        # Test creating a Part instance
        part = Part(
            access_key="PART-001",
            manufacturer_id="M001",
            manufacturer_sku="ACME-P123",
            client_sku="CLIENT-PART1",
            description="Replacement part for control unit",
            datasheet={"material": "Aluminum", "weight": "1.2kg"}
        )
        self.assertEqual(part.access_key, "PART-001")
        self.assertEqual(part.manufacturer_id, "M001")
        self.assertEqual(part.manufacturer_sku, "ACME-P123")
        self.assertEqual(part.client_sku, "CLIENT-PART1")
        self.assertEqual(part.description, "Replacement part for control unit")
        self.assertEqual(part.datasheet["material"], "Aluminum")
        self.assertEqual(part.datasheet["weight"], "1.2kg")

if __name__ == '__main__':
    unittest.main()
# This is a placeholder for actual unit tests.
# You can replace the content of this file with your actual unit tests.
