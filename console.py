#!/usr/bin/python3

import cmd
import string, sys
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage

list_classes = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    """
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt ='(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit(1)

    def do_EOF(self, line):
        """End Of File\n"""
        return True
    
    def emptyline(self):
        """Empty line\n"""
        pass

    def do_create(self, line):
        """
        """
        if (line == "" or line is None):
            print("** class name missing **")

        elif (line not in list_classes):
            print("** class doesn't exist **")

        else:
            line_to_input = f'{line}()'
            instance = eval(line_to_input)
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Show string representation
        of an instance based on the class name
        and id\n"""
        lists = line.split()
        if (line == "" or line is None):
            print("** class name missing **")

        elif (line not in list_classes):
            print("** class doesn't exist **")
        
        elif len(list) != 2:
            print("** instance id missing **")
        
        else:
            key = f'{lists[0]}.{lists[1]}'
            if key in FileStorage.all().keys():
                print(FileStorage.all()[key])
            else:
                print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
