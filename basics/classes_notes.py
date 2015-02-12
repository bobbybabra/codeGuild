###### 	classes   #########
#### 	make more arbitrary data structure with
###### 	complex structure
###	instance: the making, but not the info itself

Pet = ['fluffy' , 'poodle']

class Pet():		##### this will point to an instance
    def __init__(self, name="unkown", species="none"): ## if default values explicit, they need to made for each
        self.name = name  #like a map and self allows to point within this object
	self.species = species
	self.indoor = False ## will be False, unless specified

    def getName(self):
	return self.name

    def __str__(self):
	return "%s is a %s" % (self.name, self.species)

kit = Pet("kitty","cat")
polly = Pet("Polly" , "Parrot")
buddy = Pet(species="llama") ## explicity give where to assign, otherwise it will go to first assignment
print(polly.name)
print(polly.species)
print kit.name
kit.name = 'the kitten'
print kit.name

print polly ## calls the __str__ fxn

##########3
# 4215
# classes makes an object while fxns is a single iteration
# 

