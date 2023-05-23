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

    def test_save(self):
        obj = City()
        self.storage_1.new(obj)
        self.storage_1.save()
        with open('file.json', 'r') as file:
            data = json.load(file)
            self.assertIn("City.{}".format(obj.id), data)

    def test_reload(self):  
        obj = City()
        self.storage_1.new(obj)
        self.storage_1.save()
        self.storage_1.reload()     
        objs = FileStorage.__objects
        self.assertIn("City.{}".format(obj.id), objs)

if __name__ == '__main__':
    unittest.main()    
