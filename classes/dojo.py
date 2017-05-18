import random
from room import Room, Office, Living_spaces
from person import Person, Fellow,Staff
class Dojo(object):

	def __init__(self):
		self.offices = []					#list of all create offices
		self.living_spaces = [] 			#list of all created living
		self.unoccupied_living = []
		self.allocations_offices = {}		#offices with no. of occupants
		self.allocations_living = {}		#living with no. occupants
		self.allocated_office = {}			#stores allocated people with coreesponding room			
		self.allocated_living = {}			#stores allocated people with coreesponding room
		self.all_people = []
		self.unallocated = []

	def create_room(self, room_type, room_list):
		
		if room_type == 'office':
			for each in room_list:
				if each not in self.offices and each not in self.living_spaces:
					new_room = Office(each)
					self.offices.append(each)
					messeage = print ("An Office called", each , "has been created")
					return messeage
				else:
					print ("Room name",each ,"already in use")
		else:
			for each in room_list:
				if each not in self.offices and each not in self.living_spaces:
					new_room = Living_spaces(each)
					self.living_spaces.append(each)
					print ("A Living Space called", each , "has been created")
				else:
					print ("Room name",each ,"already in use")			

	def update_room(self):

		for room in self.offices:
			if room not in self.allocations_offices:
				self.allocations_offices.update({room : 0})

		

		for room in self.living_spaces:
			if room not in self.allocations_living:
				self.allocations_living.update({room : 0})



	def allocate_office(self, person_name):

		self.update_room()
		offices_to_let = []

		for each_room in self.allocations_offices.keys():
			if self.allocations_offices[each_room] < 7:	
				offices_to_let.append(each_room)


		if len(offices_to_let) > 0:

			allocate = random.choice(offices_to_let)
			self.allocated_office.update({person_name : allocate})
			self.allocations_offices[allocate] = self.allocations_offices[allocate] + 1
			print ("An office", allocate, "has been allocated to", person_name,)
			

		else:
			self.unallocated.append(person_name)

	def allocate_living(self,person_name):

		self.update_room()
		living_to_let = []

		for each_room in self.allocations_living.keys():
			if self.allocations_living[each_room] < 5:
				living_to_let.append(each_room)


		if len(living_to_let) > 0 :

			allocate = random.choice(living_to_let)
			self.allocated_living.update({person_name : allocate})
			self.allocations_living[allocate] = self.allocations_living[allocate] + 1
			print ("A living space ",allocate ,"has been allocated to ",person_name,) 
			

		else:
			self.unallocated.append(person_name)



	def addFellow(self,person_name,accomodation):

		if person_name not in self.all_people:
			self.all_people.append(person_name)
			print ("Fellow",person_name,"has been succesfully added !")
			new_person = Fellow(person_name)

			if accomodation == 'Y':
				self.allocate_office(person_name)
				self.allocate_living(person_name)
			else:
				self.allocate_office(person_name)
		else:
			print (person_name, "has already been added")



	def addStaff(self,person_name):

		if person_name not in self.all_people:

			self.all_people.append(person_name)
			print("Staff",person_name,"has been succesfully added !")
			#create fellow object
			self.allocate_office(person_name)
		else:
			print ( person_name,"has already been added")

	def print_room(self,room_name):

		for key in self.allocated.keys():
			if key == room_name:
				print (self.allocated[key])


	def print_allocations(self):
		
		for key in self.allocated_office.keys():
			name = key
			room =self.allocated_office[key]
			print (room, name)

		for key in self.allocated_living.keys():
			name = key
			room =self.allocated_living[key]
			print (room, name)


	def print_unallocated(self):
		
		print (self.unallocated)

	def print_allocations_to_file(self,filename):
		target = open(filename , 'w')
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


	def print_unallocations_to_file():
		target = open(filename , 'w')
		for name in self.unallocated:
			target.write(name)

		target.close()


new = Dojo()
new.create_room('office', ['andela'])

