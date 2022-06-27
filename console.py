#!/usr/bin/python3

import cmd
import string, sys

class CLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt ='(hbnb)'

    def help_hello(self):
        print ("syntax: hello [message]")
        print ("__ prints a hello message")

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, line):
        return True

    def help_quit(self):
        print ("syntax: quit",)
        print ("__ terminates the application")

    do_q = do_quit

cli = CLI()
cli.cmdloop()
