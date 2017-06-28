import random
from room import Room, Office, Living_spaces
from person import Person, Fellow, Staff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models import People, Rooms

class Dojo(object):

    def __init__(self):
        self.offices = []  # list of all create offices
        self.living_spaces = []  # list of all created living
        self.allocations_offices = []  # offices with no. of occupants
        self.allocations_living = []  # living with no. occupants
        self.all_people = []
        self.unallocated_office = []
        self.unallocated_living = []


    def create_room(self, room_type, room_list):

        found = False
        if room_type == 'office':
            for each in room_list:
                for each_object in self.offices + self.living_spaces:
                    if each_object.name == each:
                        found = True
                    else:
                        found = False

                if found == False:
                    new_room = Office(each)
                    self.offices.append(new_room)
                    print("An Office called", new_room.name, "has been created")

                else:
                    print("Room name", each, "already in use")
        else:
            for each in room_list:
                for each_object in self.offices + self.living_spaces:
                    if each_object.name == each:
                        found = True
                    else:
                        found = False

                if found == False:
                    new_room = Living_spaces(each)
                    self.living_spaces.append(new_room)
                    print("A Living Space called", new_room.name, "has been created")
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

        for person in self.all_people:
            if person_name == person.name:
                name_person = person

        if len(self.allocations_offices) > 0:
            allocate = random.choice(self.allocations_offices)
            allocate.occupants.append(name_person)
            name_person.office = allocate
            print("An office", allocate.name, "has been allocated to", name_person.name,)
        else:
            self.unallocated_office.append(name_person)
            print("No offices to allocate")


    def allocate_living(self, person_name):

        self.update_room()

        for person in self.all_people:
            if person_name == person.name:
                name_person = person


        if len(self.allocations_living) > 0:
            allocate = random.choice(self.allocations_living)
            allocate.occupants.append(name_person)
            name_person.living = allocate
            print("A living space ", allocate.name, "has been allocated to ", name_person.name,)
        else:
            self.unallocated_living.append(person_name)
            print ("No living space to allocate")


    def add_person(self, person_name, position, accomodation):
        found = False
        for person in self.all_people:
            if person.name == person_name:
                found = True

            else:
                found = False

        if found == False:
            if position == 'fellow':
                new_person = Fellow(person_name)
                print ("Person Added")
                self.all_people.append(new_person)
                if accomodation == 'Y':
                    self.allocate_office(person_name)
                    self.allocate_living(person_name)
                else:
                    self.allocate_office(person_name)
            elif position == 'staff':
                new_person = Staff(person_name)
                self.all_people.append(new_person)
                self.allocate_office(person_name)
                if accomodation == 'Y':
                    print("Staff cannot be allocated a living space")

        else:
            print(person_name, "has already been added")

    def print_room(self, room_name):

        for room in self.offices or self.living_spaces:
            if room_name == room.name:
                for person in room.occupants:
                    print (person.name)

    def print_allocations(self):

        for room in self.offices:
            print (room.name)
            if len(room.occupants) > 0:
                for member in room.occupants:
                    print (member.name)
            else:
                print ("Room Empty")

        for room in self.living_spaces:
            print (room.name)
            if len(room.occupants) > 0:
                for member in room.occupants:
                    print (member.name)
            else:
                print ("Room Empty")
    def print_unallocated(self):

        print(self.unallocated_office)
        print(self.unallocated_living)


    def print_allocations_to_file(self, filename):
        target = open(filename,'w+')
        target.truncate()

        for room in self.offices:
            target.write(room.name)
            target.write("\n")
            if len(room.occupants) > 0:
                for member in room.occupants:
                    target.write(member.name)
                    target.write("\n")
            else:
                target.write("No Occupants")

        for room in self.living_spaces:
            target.write(room.name)
            target.write("\n")
            if len(room.occupants) > 0:
                for member in room.occupants:
                    target.write(member.name)
                    target.write("\n")
            else:
                print("No Occupants")

        target.close()

    def print_unallocations_to_file(self, filename):
        target = open(filename, 'w+')
        target.truncate()
        for name in self.unallocated_living:
            target.write(name)
            target.write("\n")

        for name in self.unallocated_office:
            target.write(name)
            target.write("\n")

        target.close()


    def reallocate_person(self, person_name, new_room):
        found_person = True
        found_room = True
        all_rooms = self.offices + self.living_spaces

        for person in self.all_people:
            if person_name == person.name:
                r_name = person
                found_person = True

        for each_object in all_rooms:
            if new_room == each_object.name:
                new_room = each_object
                found_room = True

        if found_room is True and found_person is True:
            if r_name.name in self.unallocated_office or self.unallocated_living:
                    print ("Unallocated Person cannot be reallocated")
            else:
                if isinstance(new_room, Office):

                    r_name.office.occupants.remove(r_name)
                    new_room.occupants.append(r_name)
                    print(r_name.name ,"has been realloated to", new_room.name)


                if isinstance(new_room, Living_spaces):
                    r_name.living.occupants.remove(r_name)
                    new_room.occupants.append(r_name)
                    print(r_name.name ,"has been realloated to", new_room.name)
        else:
            print("Person or Room not found ")

    def load_people(self, file):
        with open(file, 'r') as file:

            file_content = file.readlines()

            for line in file_content:
                information = line.split()
                first_name = information[0]
                second_name = information[1]
                name = first_name + ' ' + second_name
                person_role = information[2].lower()

                try:
                    staying = information[3].upper()

                except:
                    staying = 'N'
                self.add_person(name, person_role, staying)

    def save_state(self, db):


        engine = create_engine('sqlite:///%s' % db)

        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)

        Base.metadata.bind = engine
        session = Session()

        for person in self.all_people:
            new_person = People()
            new_person.name = person.name
            if isinstance(person,Staff):
                new_person.role = 'staff'
                if person.office is None:
                    new_person.office = None
                else:
                    new_person.office = person.office.name
            elif isinstance(person,Fellow):
                new_person.role = 'fellow'
                if person.office is None:
                    new_person.office = None
                else:
                    new_person.office = person.office.name
                if person.living is None:
                    new_person.living = None
                else:
                    new_person.living = person.living.name
            for unallocated_person in self.unallocated_office:
                if unallocated_person == new_person.name:
                    new_person.unallocated = 'office'
            for unallocated_person in self.unallocated_living:
                if unallocated_person == new_person.name:
                    new_person.unallocated = 'living'


            session.merge(new_person)
            session.commit()

        for room in self.offices:
            new_room = Rooms()
            new_room.room_name = room.name
            new_room.category = "office"
            session.merge(new_room)
            session.commit()

        for room in self.living_spaces:
            new_room = Rooms()
            new_room.room_name = room.name
            new_room.category = "living"
            session.merge(new_room)
            session.commit()

        print ("Data saved ")

    def load_state(self, db):


        engine = create_engine('sqlite:///%s' % db)

        engine = create_engine('sqlite:///dojo_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        everyone = session.query(People).all()
        all_rooms = session.query(Rooms).all()

        for room in all_rooms:
            room_name = room.room_name
            if room.category == 'office':
                office_object = Office(room_name)
                self.offices.append(office_object)
            elif room.category == 'living':
                living_object = Living_spaces(room_name)
                self.living_spaces.append(living_object)

        for people in everyone:
            person_name = people.name
            office = people.office
            living = people.living
            if people.role == 'staff':
                person_object = Staff(person_name)
                self.all_people.append(person_object)
                for room in self.offices:
                    if people.office == room.name:
                        person_object.office = room
                        room.occupants.append(person_object)
            elif people.role == 'fellow':
                person_object = Fellow(person_name)
                self.all_people.append(person_object)
                for room in self.offices:
                    if people.office == room.name:
                        person_object.office = room
                        room.occupants.append(person_object)

                for room in self.living_spaces:
                    if people.living == room.name:
                        person_object.living = room
                        room.occupants.append(person_object)


            if people.unallocated == 'office':
                self.unallocated_office.append(person_object)
            elif people.unallocated == 'living':
                self.unallocated_living.append(person_object)
