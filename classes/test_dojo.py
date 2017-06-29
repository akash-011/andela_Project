import unittest
from dojo import Dojo
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models import People, Rooms

class TestDojo(unittest.TestCase):

    def setUp(self):
        self.new = Dojo()

    def test_check_one_office_Added(self):
        self.new.create_room("office", ["black"])
        self.assertEqual(len(self.new.offices),1)

    def test_multiple_offices_added(self):
        self.new.create_room("office", ["black","blue","green"])
        self.assertEqual(len(self.new.offices),3)

    def test_livingspace_added(self):
        self.new.create_room('living space', ['amsterdam'])
        self.assertEqual(len(self.new.living_spaces),1)

    def test_multiple_living_spaces(self):
        self.new.create_room('living space', ['amsterdam','london'])
        self.assertEqual(len(self.new.living_spaces),2)

    def test_cant_create_same_office_twice(self):
        self.new.create_room('office', ['amsterdam'])
        self.new.create_room('office', ['amsterdam'])
        self.assertEqual(len(self.new.offices),1)

    def test_cant_create_same_living_twice(self):
        self.new.create_room('living space', ['amsterdam'])
        self.new.create_room('living space', ['amsterdam'])
        self.assertEqual(len(self.new.living_spaces),1)

    def test_cant_create_room_with_same_names(self):
        self.new.create_room('living space', ['amsterdam'])
        self.new.create_room('office', ['amsterdam'])
        self.assertEqual(len(self.new.living_spaces),1)

    def test_add_fellow(self):
        self.new.add_person('Akash Baga' ,'fellow','Y')
        self.assertEqual(len(self.new.all_people),1)

    def test_add_staff(self):
        self.new.add_person('Akash Baga','staff','N')
        self.assertEqual(len(self.new.all_people),1)

    def test_cant_add_same_person_again(self):
        self.new.add_person('Akash Baga','staff','N')
        self.new.add_person('Akash Baga','staff','N')
        self.assertEqual(len(self.new.all_people),1)

    def test_cant_add_same_staff_again(self):
        self.new.add_person('Akash Baga','staff','N')
        self.new.add_person('Akash Baga','staff','N')
        self.assertEqual(len(self.new.all_people),1)

    def test_allocated_office(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        members = self.new.offices[0].occupants
        self.assertEqual(len(members),1)

    def test_allocated_living(self):
        self.new.create_room('living',['jbo'])
        self.new.add_person('Joe','fellow','Y')
        members = self.new.living_spaces[0].occupants
        self.assertEqual(len(members),1)


    def test_print_allocations_to_file(self):
        self.new.create_room('living',['jbo'])
        self.new.add_person('Joe','fellow','Y')
        self.new.print_allocations_to_file('allocations.txt')
        self.assertTrue(os.path.exists("allocations.txt"))
        os.remove('allocations.txt')

    def test_print_unllocations_to_file(self):
        self.new.create_room('living',['jbo'])
        self.new.add_person('Joe','fellow','Y')
        self.new.print_unallocations_to_file('unallocations.txt')
        self.assertTrue(os.path.exists("unallocations.txt"))
        os.remove('unallocations.txt')



    def test_unallocated_person(self):
        self.new.add_person('Joe','staff','N')
        self.assertEqual(len(self.new.unallocated_office),1)



    def test_unallocated_no_unallocated_person(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        self.assertEqual(len(self.new.unallocated_office),0)

    def test_reallocate_person_person_added(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        old_office = self.new.offices[0]
        self.new.create_room('office',['ams'])
        new_office = self.new.offices[1]
        self.new.reallocate_person('Joe','ams')
        self.assertEqual(len(new_office.occupants),1)

    def test_reallocate_person_person_removed(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        old_office = self.new.offices[0]
        self.new.create_room('office',['ams'])
        new_office = self.new.offices[1]
        self.new.reallocate_person('Joe','ams')
        self.assertEqual(len(old_office.occupants),0)


    def test_save_state(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        self.new.save_state('dojo_db')
        self.assertTrue(os.path.exists("dojo_db"))
        os.remove('dojo_db')

    def test_save_state_data(self):
        self.new.create_room('office',['jbo'])
        self.new.add_person('Joe','staff','N')
        self.new.save_state('dojo_db')
        engine = create_engine('sqlite:///dojo_db')
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        everyone = session.query(People).all()
        all_rooms = session.query(Rooms).all()
        self.assertEqual(everyone[0].name,'Joe')


    def test_load_state_data(self):
        self.new.load_state('dojo_db')
        self.assertEqual(len(self.new.all_people),1)

    def test_load_people(self):
        self.new.create_room('office',['jbo'])
        f = open("test.txt", "a")
        f.write("Paul Pogba FELLOW Y" + "\n")
        f.close()
        self.new.load_people('test.txt')
        self.assertEqual(len(self.new.all_people),1)
        os.remove('test.txt')





if __name__ == '__main__':
    unittest.main()
