#!/usr/bin/python3

import cmd
import string, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    list_class = ["BaseModel"]
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt ='(hbnb)'

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, line):
        """End Of File"""
        print()
        return True

    def do_create(self, line):
        if line == "" or None:
            print("** class name missing **")
        elif line is not in list_class:
            print("** class doesn't exist **")
        else:
            instance = eval(f'{line}()')
            instance.save()
            print(instance.id)

    def help_quit(self):
        print ("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
