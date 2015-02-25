########################### in notebook ############################
# mix-in pattern class
#	multiple inheritance... adding functionality 
#	doesn't make objects or instances, but adds to another class
#	cons, makes muliple inheritance
#	pros, easy to add in
#
# delegation pattern
#	object in another class that adds a proxy
#	avoids multi-inheritance confusion
#	pros: better than multi inheritance
#
#####################################################################


class Animal():
	def __init __(self):
		self.type = None
		self.color = None
		self.food = None
		self.predators = None
	def make_noise(self):
		return "generic animal noises"

# factory class <above>
# everything the object is and does

types = ["fish","bird","dog"]
colors = ["brown","gray","green"]
food = ["grass","bugs","other animals"]

# factory pattern maker <below>
# makes the animals
#  this seperates object creation and definition

class AnimalFactory(object):
	def make_animal(self, name, color, food, predator):
	 	animal = Animal()
	 	animal.name = name
		animal.color = color
		animal.food == food
		animal.predators = predators
		return animal

# >>> factory = animalFactory()
# >>> bear = factory.make_animal('bear','brown','fish','hunter')

for type.color, food in list(types, colors, food):
	print(types, colors, food)

# loops through factory to make instances

#-------------------------------------------------------------

# singleton class
# with methods and attributes
# make a single object instance
# good for managing other classes or methods

#-------------------------------------------------------------

# observer pattern

