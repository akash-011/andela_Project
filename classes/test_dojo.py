import unittest 
from dojo import Dojo


class TestRoomAdded(unittest.TestCase):

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
		self.new.addFellow('Akash Baga' , 'Y')
		self.assertEqual(len(self.new.all_people),1)


if __name__ == '__main__':
    unittest.main()


