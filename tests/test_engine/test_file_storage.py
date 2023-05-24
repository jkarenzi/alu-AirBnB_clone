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


if __name__ == '__main__':
    unittest.main()    
