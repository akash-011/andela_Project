from room import Room 

class Person(object):

	def __init__(self):
		pass

	def add_person(self,name,position,accomodation):
		self.name = name 
		self.position = position
		self.accomodation = accomodation
		if self.position == 'fellow' and self.accomodation == 'Y':
			#call accomodate
			#call allocate
			#append to fellow
		elif self.position == 'fellow' and self.accomodation == 'N':
			#add to unallocated_living
			#call allocate_office
			#append to fellow
		elif self.position == 'staff':
			#call allocate_office
			#append to staff





