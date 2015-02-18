import random


class Character():
    def __init__(self, name, life):
        self.name = "placeholder"
        self.life = life
        self.weapon = []

    def takehit(self, hit):
        self.life -= hit
        if self.life <= 0:
            print(self.name + " is dead")

    def makelife(self, snack):
        self.life += snack


class Player(Character):
    def __init__(self):
        Character.__init__(self, name=" ", life=100)
        if self.life <= 0:
            print (self.name + " roams among the undead and craves BRAINS!!")

    def quit(self):
        print "quit"

    def menu(self):
        print menu.keys

    def takeweapon(self):
        pass

    def snack(self):
        self.life += 10
        print "eat"

    def attack(self):
        print "attack"

    def run(self):
        print 'run'


class Zombie(Character):
    def __init__(self):
        Character.__init__(self, name, life)
        self.name = "a " + zom_adj + " " + antagonist + " zombie" 
        self.life = 30
        self.monster = []

        self.zom_adj = random.choice['wretched', 'filthy', 'disgusting', 'oozing']
        self.antagonist = random.choice["football" , "cheerleader" , "emo kid"]

#def main():
#print "Action Menu:"
print "-" * 20
menu = {
    "quit" : Player.quit,
    "menu" : Player.menu,
    "take weapon" : Player.takeweapon,
    "eat victual" : Player.snack,
    "attack" : Player.attack,
    "flee" : Player.run,
}

h = Player()
h.name = raw_input("What is your character name?\n>")
print """\t\tZOMBIE HIGH SCHOOL!\n"""
print "type 'menu' to get a menu of actions you can take.\n"

while h.life > 0:
    line = raw_input("> ")
    if 'qu' in line:
        Player.quit()
    elif 'men' in line:
        x = Player()
        x.menu()
    elif 'tak' in line:
        Player.takeweapon()
    elif 'eat' in line:
        Player.snack()
    elif 'at' in line:
        Player.attack()
    elif 'fl' in line:
        Player.run()
    else:
        print "Bewildered and confused, try another action"
    # for x in menu.keys():
    #     if x in line:
    #         menu[x](input)
    #     else:
    #         print "try again"

#main()