
"""
This uses docopt to build a command line interface for the Dojo room allocater system

Usage:
    dojo create_room (office | living) <room name>...
    dojo add_person  <first_name> <last_name> (fellow | staff) [--accomodation=(y|n)]
    dojo print_room <room_name>
    dojo print_allocated [-o = <filename>]
    dojo print_uncallocated [-o = <filename>]
    dojo reallocate_person <first_name> <last_name> <room_name>
    dojo load_people <filename>
    dojo save_state [-d = <db_name>]
    dojo load_state <db_name>
    dojo (-i | --interactive)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.




"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo


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
    def intro():
        print(__doc__)


    intro = intro()
    prompt = '(Dojo) '
    file = None


    @docopt_cmd

    def do_create_room(self, arg):
        """Usage: create_room (office|living) <room_name>... """

        if arg['office'] is True:
            room_type = 'office'
        elif arg['living'] is True:
            room_type = 'living'

        room_list = arg['<room_name>']
        new.create_room(room_type,room_list)


    @docopt_cmd
    def do_add_person(self,arg):
        """Usage: add_person  <first_name> <last_name> (fellow | staff) [--accomodation=(y|n)]"""
        person_name = arg['<first_name>'] + " "+ arg['<last_name>']

        if arg['fellow'] == True:
            position = 'fellow'
        else:
            position = 'staff'

        if arg['y'] == True:
            living = 'Y'
        else:
            living = 'N'
        new.add_person(person_name,position,living)


    @docopt_cmd
    def do_print_room(self,arg):
        """Usage: print_room <room_name> """
        room = arg['<room_name>']
        new.print_room(room)


    @docopt_cmd
    def do_print_allocated(self,arg):
        """Usage: print_allocated [-o = <filename>] """

        if arg['-o'] is True:
            filename = arg['<filename>']
            new.print_allocations_to_file(filename)
        else:
            new.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self,arg):
        """Usage: print_uncallocated [-o = <filename>] """
        if arg['-o'] is True:
            filename = arg['<filename>']
            new.print_unallocations_to_file(filename)
        else:
            new.print_unallocated()


    @docopt_cmd
    def do_reallocate_person(self,arg):
        """Usage: reallocate_person <first_name> <last_name> <room_name>"""
        name = arg['<first_name>'] + " "+ arg['<last_name>']
        room = arg['<room_name>']
        new.reallocate_person(name,room)

    @docopt_cmd
    def do_save_state(self,arg):
        """Usage: save_state [-d = <db_name>] """
        if arg['-d'] is True:
            db = arg['<db_name>']
        else:
            db = 'dojo_db'

        new.save_state(db)


    @docopt_cmd
    def do_load_people(self,arg):
        """Usage: load_people <filename> """
        filename = arg['<filename>']
        new.load_people(filename)


    @docopt_cmd
    def do_load_state(self,arg):
        """Usage: load_state <db_name>  """
        dbname = arg['<db_name>']
        new.load_state(dbname)




    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
