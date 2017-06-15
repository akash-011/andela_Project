import random
from room import Room, Office, Living_spaces
from person import Person, Fellow, Staff


class Dojo(object):

    def __init__(self):
        self.offices = []  # list of all create offices
        self.living_spaces = []  # list of all created living
        self.unoccupied_living = []
        self.allocations_offices = []  # offices with no. of occupants
        self.allocations_living = []  # living with no. occupants
        self.allocated_living = {}  # stores allocated people with coreesponding room
        self.all_people = []
        self.unallocated = []

    def create_room(self, room_type, room_list):

        if room_type == 'office':
            for each in room_list:
                if each not in self.offices and each not in self.living_spaces:
                    new_room = Office(each)
                    self.offices.append(new_room)
                    print("An Office called", each, "has been created")

                else:
                    print("Room name", each, "already in use")
        else:
            for each in room_list:
                if each not in self.offices and each not in self.living_spaces:
                    new_room = Living_spaces(each)
                    self.living_spaces.append(new_room)
                    print("A Living Space called", each, "has been created")
                else:
                    print("Room name", each, "already in use")

    def update_room(self):

        for room in self.offices:
            if len(room.occupants) < 7:
                self.allocations_offices.append(room)

        for room in self.living_spaces:
            if len(room.occupants) < 5:
                self.allocations_living.append(room)


    def allocate_office(self, person_name):

        self.update_room()
        allocate = random.choice(self.allocations_offices)
        allocate.occupants.append(person_name)
        print("An office", allocate, "has been allocated to", person_name,)


    def allocate_living(self, person_name):
        self.update_room()
        allocate = random.choice(self.allocations_living)
        allocate.occupants.append(person_name)
        print("A living space ", allocate, "has been allocated to ", person_name,)



    def add_person(self, person_name, position, accomodation):

        if person_name not in self.all_people:
            print(position, person_name, "has been succesfully added !")
        else:
            print(person_name, "has already been added")

        if position == 'fellow':
            new_person = Fellow(person_name)
            self.all_people.append(new_person)
            if accomodation == 'Y':
                self.allocate_office(person_name)
                self.allocate_living(person_name)
            else:
                self.allocate_office(person_name)
        else:
            new_person = Staff(person_name)
            self.all_people.append(new_person)
            self.allocate_office(person_name)
            if accomodation == 'Y':
                print("Staff cannot be allocated a living space")

    def print_room(self, room_name):
        room_print = []
        if room_name in self.allocated_office.values():
            print(list(self.allocated_office.keys()))

    def print_allocations(self):

        for key in self.allocated_office.keys():
            name = key
            room = self.allocated_office[key]
            print(room, name)

        for key in self.allocated_living.keys():
            name = key
            room = self.allocated_living[key]
            print(room, name)

    def print_unallocated(self):

        print(self.unallocated)

    def print_allocations_to_file(self, filename):
        target = open(filename, 'w+')
        target.truncate()
        target.write("Room name\t\t")
        target.write("Person\n")
        for key in self.allocated_office.keys():
            room = self.allocated_office[key]
            name = key
            target.write(room)
            target.write("\t\t\t")
            target.write(name)
            target.write("\n")
        for key in self.allocated_living.keys():
            room = self.allocated_living[key]
            name = key
            target.write(room)
            target.write("\t\t\t")
            target.write(name)
            target.write("\n")

        target.close()

    def print_unallocations_to_file(self, filename):
        target = open(filename, 'w+')
        target.truncate()
        for name in self.unallocated:
            target.write(name)
            target.write("\n")

        target.close()


    def load_people(self, file):
        '''this function reads a lists of people and allocates them a room'''
        with open(file, 'r') as file:

            file_content = file.readlines()

            for line in file_content:
                information = line.split()
                first_name = information[0]
                second_name = information[1]
                name = first_name + ' ' + second_name
                person_role = information[2].lower()

                try:
                    staying = information[3]

                except:
                    staying = 'N'
                self.add_person(name, person_role, staying)
