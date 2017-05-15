class Room(object):

	def __init__(self):
		pass
		


	
	def create_room(self, room_type, room_list):
		self.room_type = room_type
		self.room_list = room_list
		room_count = 0
		offices = []
		living_spaces = []
		for room in self.room_list:
			room_count += 1
			print(room_count)
		
		if self.room_type == 'office':
			for each in self.room_list:
				offices.append(each)
				print ("room created ")
			return offices
		else:
			for each in self.room_list:
				living_spaces.append(each)
				print ("room_created2 ")
			return living_spaces


class office(Room):

	def __init__(self):
		pass 

	def allocate_office(person_name):
		self.name = name 
		allocated_offices = {}
		




	
class living_space(Room):



#create_room = Room().create_room("living_space", ["black","blue"])

