class Room(object):

	def __init__(self, name):
		self.name = name 


class Office(Room):
	def __init__(self,name):
		super(Office,self).__init__(name)



