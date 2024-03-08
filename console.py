#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter for HBNB.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter for HBNB.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Handles end of file input (Ctrl + D)
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
