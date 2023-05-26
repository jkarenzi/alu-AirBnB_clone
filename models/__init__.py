from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

storage = FileStorage()
storage.reload()
user = User()
state = State()
city = City()
# Add new objects to the file storage
storage.new(user)
storage.new(state)
storage.new(city)
# Save all objects to the JSON file
storage.save()
storage.reload()

dict_classes = {"BaseModel": BaseModel, "User": User,  "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}
