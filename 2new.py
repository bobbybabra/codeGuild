import random


class Character():
    def __init__(self, name, life):
        self.name = "placeholder"
        self.life = life

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

    def weapon(self):
        self.weapon = []

    def attack(self):
# TODO: if weapon then increase hit damage by 10
        hit = random.choice(range(1, Zombie.life)
        Zombie.life -= hit
        print "Zombie life is" + Zombie.self.life


class Zombie(Character):
    def __init__(self):
        Character.__init__(self, name, life)
        self.name = "a " + zom_adj + " " + antagonist + " zombie"
        self.life = 30
        self.monster = []

        self.zom_adj = random.choice['wretched', 'filthy', 'disgusting', 'oozing']
        self.antagonist = random.choice["football" , "cheerleader" , "emo kid"]

    def attacks(self):
        hits = random.choice(range(1, Player.life))
        Player.life -= hits
        print "Your life is now" + Player.life


def quit():
    print "The zombie virus has infected you, You are now undead and crave BRAINS!!"
    Player.health = 0

def menu():
    print help

def be_a_hero():
# TODO: make counter and once 10 zombies are slayed, you win
    print 'virtuous are the brave!!\n'
    print 'hark! %s approaches' %s Zombie.name
    Zombie.attacks()

def takeweapon(self):
    print "your friend plays softball! you grab her bat from her locker"
    for w in weapon:
        Player.weapon.append(bat)
# TODO: allow weapon option only after 3 zombies are fought then remove

def snack(self):
    Player.life += 10
    print "manga manga"
    print "Your life is now" + Player.life
# TODO: allow snack option only after 5 zombies are fought

def attack(self):
    print "die pond scum!"
    Player.attack()

def run(self):
    print 'runaway!'
    Player.life -= 5
    print "Your life is now" + Player.life


#def main():
#print "Action Menu:"
print "-" * 20
help = [
    "quit",
    "menu",
    "take weapon",
    "eat victual",
    "attack",
    "flee",
]

h = Player()
h.name = raw_input("What is your character name?\n>")
print """\t\tZOMBIE HIGH SCHOOL!\n"""
print "type 'menu' to get a menu of actions you can take.\n"

while h.life > 0:
    line = raw_input("> ")
    if 'qu' in line:
        quit()
    elif 'men' in line:
        menu()
    elif 'tak' in line:
        takeweapon()
    elif 'eat' in line:
        snack()
    elif 'at' in line:
        attack()
    elif 'fl' in line:
        run()
    else:
        print "Bewildered and confused... try another action"

#main()