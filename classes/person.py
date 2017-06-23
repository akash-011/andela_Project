class Person(object):

	def __init__(self,name):
		self.name = name
		self.office = None

class Fellow(Person):
	def __init__(self,name):
		super(Fellow,self).__init__(name)
		self.living = None
class Staff(Person):
	def __init__(self,name):
		super(Staff,self).__init__(name)
