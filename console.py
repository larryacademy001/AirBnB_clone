#!/usr/bin/python3
"""Module for HBNB console"""

import cmd
import json
from models.base_model import BaseModel
import models
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


valid_classes = {
    "BaseModel", "User", "State",
    "City", "Amenity", "Place", "Review"
}


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line method"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in valid_classes:
                print("** class doesn't exist **")
                return

            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in valid_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            key = class_name + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in valid_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            key = class_name + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg and arg not in valid_classes:
            print("** class doesn't exist **")
            return

        objects = [
            str(obj) for obj in storage.all().values()
            if not arg or obj.__class__.__name__ == arg
        ]
        print(objects)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into
        the JSON file).
        Usage: update <class name> <id> <attribute name>
        "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
        print(instance)

    def do_count(self, arg):
        """Count the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        count = 0
        objects = storage.all()
        for obj in objects.values():
            if obj.__class__.__name__ == class_name:
                count += 1

        print(count)

    def precmd(self, arg):
        if "." in arg:
            modified_argument = (
                arg.replace(".", " ")
                .replace(", ", " ")
                .replace("(", " ")
                .replace(")", " ")
                .replace('"', "")
                .replace("{", "")
                .replace("}", "")
                .replace("'", "")
                .replace(":", "")
            )
            argument_list = modified_argument.split()
            argument_list[0], argument_list[1] = \
                argument_list[1], argument_list[0]
            arg = " ".join(argument_list)

        return super().precmd(arg)

    def onecmd(self, args):
        if args == "quit":
            return self.do_quit(args)
        elif args == "EOF":
            return self.do_EOF(args)
        else:
            return cmd.Cmd.onecmd(self, args)

    @classmethod
    def handle_hbnb_command_error(cls, command_arg, **kwargs):
        if "all" in kwargs.values():
            if not command_arg:
                return False

        if not command_arg:
            print("** class name missing **")
            return True
        else:
            command_arg = command_arg.split()

        num_command_args = len(command_arg)

        if command_arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
            return True

        if "command" not in kwargs:
            return False

        for sub_command_arg in kwargs.values():
            if sub_command_arg in ["show", "destroy"]:
                if num_command_args < 2:
                    print("** instance id missing **")
                    return True

            if sub_command_arg == "update":
                if num_command_args < 2:
                    print("** instance id missing **")
                    return True
                elif num_command_args < 3:
                    print("** attribute name missing **")
                    return True
                elif num_command_args < 4:
                    print("** value missing **")
                    return True

        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
