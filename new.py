import random

class Character():
    def self.__init__(self, name, life):
        self.name = name
        self.life = life
        self.weapon = weapon

    def takeHit(self.life, hit):
        self.life -= hit
        if self.life <= 0:
            print(self.name + " is dead)

    def makeLife(self.life, snack):
        self.life += snack

class Player(Character):
    def self.__init__(self):
        self.name = name
        self.life = 100

class Zombie(Character):
    def self.__init__(self):
        self.name = "a " + zom_adj + " " + antagonist + " zombie" 
        self.life = 30

    zom_adj = random.choice['wretched', 'filthy', 'disgusting', 'oozing']
    antagonist = random.choice["football" , "cheerleader" , "emo kid"]

menu = {
    "quit" : Player.quit,
    "help" : Player.help,
    "take weapon" : Player.takeWeapon,
    "eat victual" : Player.snack,
    "attack" : Player.attack,
    "flee" : Player.run,
}

input = Player()
input.name = raw_input("What is your character name?\n>\n")
print """\t\tZOMBIE HIGH SCHOOL!\n"""
print "type 'help' to get a menu of actions you can take.\n"

while input.life > 0 :
    line = raw_input("> ")
    for x in menu.keys():
        if x is in menu:
            menu[x](input)
        else:
            print "try again"

