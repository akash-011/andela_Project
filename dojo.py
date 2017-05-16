import random
from room import Room,Office
class Dojo(object):

	def __init__(self):
		self.offices = []
		self.living_spaces = [] 
		self.unoccupied_offices = []
		self.allocations = {}
		self.allocated = {}
	
	def create_room(self, room_type, room_list):
		
		if room_type == 'office':
			for each in room_list:
				new_room = Office(each)
				self.offices.append(each)
				print ("room created ")
		
		else:
			for each in room_list:
				living_spaces.append(each)
				print ("room_created2 ")
			return living_spaces


	def addStaff(self,person_name):

		for room in self.offices:
			if room not in self.allocations:
				self.allocations.update({room : 0})


		print (self.allocations)     #----------REMOVE_LATER

		for each_room in self.allocations.keys():
			if self.allocations[each_room] < 7:
				self.unoccupied_offices.append(each_room)

		print (self.unoccupied_offices) #----------REMOVE_LATER


		allocate = random.choice(self.unoccupied_offices)
		self.allocated.update({allocate : person_name})
		self.allocations[allocate] = self.allocations[allocate] + 1
		print("Office allocated")
		print (self.allocations)
		print (self.allocated)

	def addFellow(self,fellow_name,accomodation):
		


	def allocate_living_space(self,person_name):
		pass

	def addPerson(self):
		pass




new = Dojo()
new.create_room('office', ['black','blue'])
new.addStaff('Akash')

