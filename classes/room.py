class Room(object):

	def __init__(self, name):
		self.name = name 
		self.occupants = []


class Office(Room):
	def __init__(self,name):
		super(Office,self).__init__(name)



class Living_spaces(Room):
	def __init__(self,name):
		super(Living_spaces,self).__init__(name)