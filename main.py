"""
Usage:

main.py create_room (office | living) <room name>...

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.




"""

import sys
import cmd
from docopt import docopt, DocoptExit
from classes.dojo import Dojo


new = Dojo()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
	intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None


    @docopt_cmd
    def do_create_room(self,arg):
    	"""
    	Usage: create_room (office | living) <room name>...
    	"""
 		print (arg)















opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()


