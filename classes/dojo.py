import random
from room import Room,Office
class Dojo(object):

	def __init__(self):
		self.offices = []					#list of all create offices
		self.living_spaces = [] 			#list of all created living
		self.unoccupied_living = []
		self.allocations_offices = {}		#offices with no. of occupants
		self.allocations_living = {}		#living with no. occupants
		self.allocated = {}					#all allocated people and which room
		self.all_people = []
		self.unallocated = []

	def create_room(self, room_type, room_list):
		
		if room_type == 'office':
			for each in room_list:
				new_room = Office(each)
				self.offices.append(each)
				print ("room created ")
		
		else:
			for each in room_list:
				new_room = Office(each)
				self.living_spaces.append(each)
				print ("room_created2 ")
		

	def update_room(self):

		for room in self.offices:
			if room not in self.allocations_offices:
				self.allocations_offices.update({room : 0})

		

		for room in self.living_spaces:
			if room not in self.allocations_living:
				self.allocations_living.update({room : 0})



	def allocate_office(self, person_name):

		new.update_room()
		offices_to_let = []

		for each_room in self.allocations_offices.keys():
			if self.allocations_offices[each_room] < 7:	
				offices_to_let.append(each_room)


		if len(offices_to_let) > 0:

			allocate = random.choice(offices_to_let)
			self.allocated.update({allocate : person_name})
			self.allocations_offices[allocate] = self.allocations_offices[allocate] + 1
			print ("Office allocated")
			print (self.allocated)

		else:
			self.unallocated.append(person_name)

	def allocate_living(self,person_name):

		new.update_room()
		living_to_let = []

		for each_room in self.allocations_living.keys():
			if self.allocations_living[each_room] < 5:
				living_to_let.append(each_room)


		if len(living_to_let) > 0 :

			allocate = random.choice(living_to_let)
			self.allocated.update({allocate : person_name})
			self.allocations_living[allocate] = self.allocations_living[allocate] + 1
			print ("living allocated") 
			print (self.allocated)

		else:
			self.unallocated.append(person_name)



	def addPerson(self,person_name,position,accomodation):

		if position == 'staff':
			#create object of staff
			self.all_people.append(person_name)
			new.allocate_office(person_name)

		elif position == 'fellow' and accomodation == 'N' :
			#create object fellow
			self.all_people.append(person_name)
			new.allocate_office(person_name)

		elif position == 'fellow' and accomodation == 'Y' :
			#create object fellow
			self.all_people.append(person_name)
			new.allocate_office(person_name)
			new.allocate_living(person_name)

	def print_room(self,room_name):

		for key in self.allocated.keys():
			if key == room_name:
				print (self.allocated[key])


	def print_allocations():
		pass

	def print_unallocated():
		pass

	def print_allocations_to_file():
		pass

	def print_unallocations_to_file():
		pass
"""

	





"""


new = Dojo()
new.create_room('office', ['black','blue'])
new.create_room('living space', ['green'])
new.addPerson('Akash','fellow','Y')
new.print_room('green')

