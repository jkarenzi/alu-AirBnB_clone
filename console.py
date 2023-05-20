#!/usr/bin/python3
"""
This module helps us create a command interpreter 
for the airbnb project
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """class for the console, inheriting from cmd.Cmd"""
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        """command for exiting the program."""
        return True

    def do_EOF(self, arg):
        """Exiting the program with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Doing nothing on an empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()  
      