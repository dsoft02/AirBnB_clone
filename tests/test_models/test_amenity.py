import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_Model(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instantiation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_inherits_from_BaseModel(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_name_attribute_default(self):
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
