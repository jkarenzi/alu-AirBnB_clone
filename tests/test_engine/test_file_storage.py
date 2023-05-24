#!/usr/bin/python3
"""test for the FileStorage class"""

import models
import os
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
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}    

    def test_all(self):
        self.assertIsInstance(models.storage.all(), dict)
        
    def test_new(self):
        obj = State()
        all_objects = models.storage.all()
        self.assertIn("State.{}".format(obj.id), all_objects)

    def test_save(self):
        obj1= BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = Place()
        obj5 = City()
        obj6 = Amenity()
        obj7 = Review()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.new(obj3)
        models.storage.new(obj4)
        models.storage.new(obj5)
        models.storage.new(obj6)
        models.storage.new(obj7) 
        models.storage.save()
        with open("file.json", "r") as file:
            json_data = file.read()
            self.assertIn("BaseModel." + obj1.id, json_data)
            self.assertIn("User." + obj2.id, json_data)
            self.assertIn("State." + obj3.id, json_data)
            self.assertIn("Place." + obj4.id, json_data)
            self.assertIn("City." + obj5.id, json_data)
            self.assertIn("Amenity." + obj6.id, json_data)
            self.assertIn("Review." + obj7.id, json_data)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        x = BaseModel()
        y = User()
        z = State()
        a = Place()
        b = City()
        c = Amenity()
        d = Review()
        models.storage.new(x)
        models.storage.new(y)
        models.storage.new(z)
        models.storage.new(a)
        models.storage.new(b)
        models.storage.new(c)
        models.storage.new(d)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + x.id, objs)
        self.assertIn("User." + y.id, objs)
        self.assertIn("State." + z.id, objs)
        self.assertIn("Place." + a.id, objs)
        self.assertIn("City." + b.id, objs)
        self.assertIn("Amenity." + c.id, objs)
        self.assertIn("Review." + d.id, objs)
    
    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)            


if __name__ == '__main__':
    unittest.main()    
