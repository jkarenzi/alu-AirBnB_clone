#!/usr/bin/python3
"""test for the FileStorage class"""

import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage_1 = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage_1.all(), dict)
        
    def test_new(self):
        obj = State()
        all_objects = self.storage_1.all()
        self.assertIn("State.{}".format(obj.id), all_objects)

    def test_save_and_reload(self):
        # Create some objects to save
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = City()
        obj5 = Place()
        obj6 = Amenity()
        obj7 = Review()

        # Add objects to the storage
        self.storage_1.new(obj1)
        self.storage_1.new(obj2)
        self.storage_1.new(obj3)
        self.storage_1.new(obj4)
        self.storage_1.new(obj5)
        self.storage_1.new(obj6)
        self.storage_1.new(obj7)

        # Save the objects
        self.storage_1.save()

        # Clear the objects in storage
        self.storage_1._FileStorage__objects = {}

        # Reload the objects
        self.storage_1.reload()

        # Check if objects were reloaded correctly
        self.assertIn("BaseModel.{}".format(obj1.id), self.storage_1.all())
        self.assertIn("User.{}".format(obj2.id), self.storage_1.all())
        self.assertIn("State.{}".format(obj3.id), self.storage_1.all())
        self.assertIn("City.{}".format(obj4.id), self.storage_1.all())
        self.assertIn("Place.{}".format(obj5.id), self.storage_1.all())
        self.assertIn("Amenity.{}".format(obj6.id), self.storage_1.all())
        self.assertIn("Review.{}".format(obj7.id), self.storage_1.all())

        # Check if reloaded objects have the correct attributes
        self.assertEqual(self.storage_1.all()["BaseModel.{}".format(obj1.id)].id, obj1.id)
        self.assertEqual(self.storage_1.all()["User.{}".format(obj2.id)].id, obj2.id)
        self.assertEqual(self.storage_1.all()["State.{}".format(obj3.id)].id, obj3.id)
        self.assertEqual(self.storage_1.all()["City.{}".format(obj4.id)].id, obj4.id)
        self.assertEqual(self.storage_1.all()["Place.{}".format(obj5.id)].id, obj5.id)
        self.assertEqual(self.storage_1.all()["Amenity.{}".format(obj6.id)].id, obj6.id)
        self.assertEqual(self.storage_1.all()["Review.{}".format(obj7.id)].id, obj7.id)


if __name__ == '__main__':
    unittest.main()    
