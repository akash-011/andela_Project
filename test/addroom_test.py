import unittest 
from room import Dojo

class TestRoomAdded(unittest.TestCase):

	def setUp(self):
		self.room = Dojo()

	def check_One_Room_Added(self):
		result = self.room.create_room("office", ["black"])
		self.assertEqual(['black'],result)

	def check_multiple_rooms_added(self):
		result = self.room.create_room('office', ['black','blue'])
		self.assertEqual(result,['black','blue'])

if __name__ == '__main__':
    unittest.main()


