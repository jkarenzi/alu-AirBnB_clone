import cmd
"""
This module helps us create a command interpreter for the airbnb project
"""

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'


if __name__ == "__main__":
    HBNBCommand().cmdloop()  
      