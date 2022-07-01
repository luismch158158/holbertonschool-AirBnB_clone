#!/usr/bin/python3

import cmd
import string
import sys
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

list_classes = ["BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]


def parser_list(lists):
    """this function parses a list that is of type string into a
    true list by decomposing each element and inserting
    into a new list
    Return: New List"""
    lista = lists[1:-1].replace("\"", "")
    lista = lista.split(", ")
    return lista


def isfloat(num):
    """This function evaluates if a number
    is a float or not a float and returns
    True if it is a float and False if not."""
    try:
        float(num)
        return True
    except ValueError:
        return False


def parser(lista):
    """This function parses the elements of a list if
    it is a string it removes the quotes and if it does
    not have quotes it keeps it the same, at the
    end it returns a parsed list"""
    final_list = []
    for i in lista:
        if (i[0] == '\"'):
            final_list.append(i[1:-1])
        else:
            final_list.append(i)
    return final_list


def validator(lists):
    """They are a valid function if what they are passing
    me is a list or has quotes to be able to parse it and
    return a set element with the correct type to be
    inserted in the dictionary later"""
    new_list = []
    lista_principal = []
    total = len(lists)
    print(lists)
    new_member = lists[3]
    if (lists[3][0] == '\"' or lists[3][0] == '['):
        for i in range(total):
            if i >= 3:
                new_list.append(lists[i])
            else:
                lista_principal.append(lists[i])
        new_str = " ".join(new_list)
        lista_principal.append(new_str)
        lists = lista_principal
        if (lists[3][0] == '\"'):
            new_member = lists[3][1:-1]
        else:
            new_member = lists[3]
    return new_member


class HBNBCommand(cmd.Cmd):
    """Command Interpreter of Airbnb"""

    def __init__(self):
        """Constructor of Command Interpreter"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def default(self, line):
        """Function of the HBNB command that executes
        functions by default before all functions"""
        lists = line.split(".")
        lista = lists[1].split("(")
        string = lista[-1].replace(")", "")
        lista_f = list(string.split(", "))
        final = [lista[0], lists[0]]
        final = final + lista_f

        if final[0] == "all":
            line = final[1]
            """Retrieve all instances of a class by using:
            <class name>.all()"""
            HBNBCommand.do_all(self, line)

        elif final[0] == "count":
            line = final[1]
            """retrieve the number of instances of a class:
            <class name>.count()"""
            HBNBCommand.do_count(self, line)

        elif final[0] == "show":
            line = parser(final[1:])
            line = " ".join(line)
            """retrieve an instance based on its ID:
            <class name>.show(<id>)"""
            HBNBCommand.do_show(self, line)

        elif final[0] == "destroy":
            line = parser(final[1:])
            line = " ".join(line)
            """destroy an instance based on his ID:
            <class name>.destroy(<id>)"""
            HBNBCommand.do_destroy(self, line)

        elif final[0] == "update":
            line = parser(final[1:])
            line = " ".join(line)
            """update an instance based on his ID:
            <class name>.update(<id>, <attribute name>, <attribute value>)"""
            HBNBCommand.do_update(self, line)

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
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
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

        elif (lists[0] not in list_classes):
            print("** class doesn't exist **")

        elif len(lists) != 2:
            print("** instance id missing **")

        else:
            key = f'{lists[0]}.{lists[1]}'
            if key in models.storage.all().keys():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id"""
        lists = line.split()
        if (line == "" or line is None):
            print("** class name missing **")

        elif (lists[0] not in list_classes):
            print("** class doesn't exist **")

        elif len(lists) != 2:
            print("** instance id missing **")

        else:
            key = f'{lists[0]}.{lists[1]}'
            if key in models.storage.all().keys():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the classname"""
        lists = line.split()

        new_list = []

        if len(lists) < 1:
            for member in models.storage.all().values():
                new_list.append(str(member))
            print(new_list)
        else:
            if (lists[0] in list_classes):
                for member in models.storage.all():
                    if re.search(lists[0], member):
                        print(models.storage.all()[member])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)"""
        lists = line.split()
        total = len(lists)

        ints = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
        floatings = ["latitude", "longitude"]

        if (line == "" or line is None):
            print("** class name missing **")
            return
        if (lists[0] not in list_classes):
            print("** class doesn't exist **")
            return
        if len(lists) == 1:
            print("** instance id missing **")
            return

        else:
            key = f'{lists[0]}.{lists[1]}'
            if key in models.storage.all().keys():
                if len(lists) >= 3:
                    if len(lists) >= 4:
                        print(lists[3])
                        new_member = validator(lists)
                        lists[3] = new_member
                        if lists[0] == "Place":
                            if lists[2] in ints and lists[3].isdigit():
                                lists[3] = int(lists[3])
                            elif (lists[2] in floatings and isfloat(lists[3])):
                                lists[3] = float(lists[3])
                            elif lists[3][0] == "[":
                                lists[3] = parser_list(lists[3])
                            elif (lists[2] not in ints
                                  ) and (lists[2] not in floatings):
                                setattr(models.storage.all()[key],
                                        lists[2], lists[3])
                                models.storage.all()[key].save()
                        setattr(models.storage.all()[key], lists[2], lists[3])
                        models.storage.all()[key].save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        lists = line.split()
        count = 0
        for classes in models.storage.all().values():
            if lists[0] == classes.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
