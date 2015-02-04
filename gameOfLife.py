''' 
The Game of Life: 
Hey, we all make choices and, well,
they have consequences.  So here we go, 
life is like baseball and baseball is a game, 
so here it is: 
The Game of life
'''
print ('The Game of Life
	We'll start at the summer
	before high school....')

name = raw_input('what\s you name:\n' )
gender = raw_input('boy or girl? (b/g)\n' )
 
print job_prompt

car = False

def main():
    health = 80
    intel = 50
    charisma = 30
    status = 30

main()
    
class Character():
    def __init__(self, name , gender):
	self.name = name
	self.gender = gender
	self.orientation = True
	self.age = 14

	graduate  = 18
	year_pass = 1
	while age <= 4:
	    print "Welcome to the next year of high school"
	    age += year_pass
		if age == graduate:
		    print 'congradulatons, you are a high school graduate!'
	                break

    def getName(self):
	return self.name

    def getAge(self):
	return self.age

    def __str__(self):
	return "Hi %s" % self.name

class Family():
    def __init__(self):
	self.mom = True
	self.dad = True
	self.pet = True
	self.olderBrother = True
	self.youngerSister = True
	self.unPlannedNewborn = False
	self.unknownUncle = False

class Health():
    def __init__(self, fitness , exercise , food , drink , mood, snack , drug):
	self.fitness = fitness
	self.exercise = exercise
	self.food = food
	self.drink = drink
	self.mood = mood
	self.snack = snack
	self.drug = drug
	self.depressed = False

    def getFitness():
	return self.fitness

    def getExercise():
	return self.exercise

    def getFood():
	return self.food

    def getDrink():
	return self.drink

    def getMood():
	return self.mood

    def getSnack():
	return self.snack

    def getDrug():
	return self.drug

class Work():

    job = []
    hobby = []
    timeWaste = []
    
    def add_hobby(self, *hobbies):
        for hobby in hobbies:
            self.hobbies.append(hobby)
        return self.hobbies

    def __str__(self):
	return "%s, you need a job! \n" %self.name
	in_out = raw_input("would you like to work inside or outside? \ni/o>")
	    if in_out.lower == 'i'
		pass
	    if in_out.lower == 'o'
		pass
