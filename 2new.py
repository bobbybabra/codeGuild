import random


class Character():
    def __init__(self, name, life):
        self.name = ""
        self.life = life

    def takehit(self, hit):
        self.life -= hit
        if self.life <= 0:
            print(self.name + " is dead")

    # def makelife(self, snack):
    #     self.life += snack


class Player(Character):
    def __init__(self):
        Character.__init__(self, name=" ", life=100)
        if self.life <= 0:
            print (self.name + " roams among the undead and craves BRAINS!!")

    def set_kills(self):
        zombie_kills = 0
        self.zk = zombie_kills

    def weapon(self):
        self.weapon = weapon

    def attack(self):
        hit = random.choice(range(1, Zombie.life))
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

zombie_kills = 0
h = Player()


class Action(Player):
#    act = Player()
#    act.set_kills()

    def quit(self):
        print "The zombie virus has infected you, You are now undead and crave BRAINS!!\n"
        print "Unless you are a vegetarian, then you crave...GRAINS!!\n\n"
        h.life = 0
        quit()

    def menu(self):
        if zombie_kills <= 4:
            print menu_one()
        elif zombie_kills >= 5:
            print menu_two()
        elif zombie_kills >= 10:
            print menu_three()

    def be_a_hero(self):
    # TODO: make counter and once 10 zombies are slayed, you win
        print 'virtuous are the brave!!\n'
        print ('hark! %s approaches') %sZombie().name
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
    # TODO: make menu list, if run < 1 print no exit... etc.
        print 'runaway!'
        Player.life -= 5
	bad_exit = "you bolt out the door and enter the corridor, the hallway is chaos and you notice the exit is blocked by zombies eating your classmates"
	if zombie_kills <= 1
		print bad_exit
	elif
        print "Your life is now" + Player.life


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def menu_one():
    print "Action Menu:"
    print "-" * 30
    print("quit")
    print("menu")
    print( "look around")
    print( "attack")
    print("flee")
    print "-" * 30


def menu_two():
    print "Action Menu:"
    print "-" * 30
    print("quit")
    print("menu")
    print( "take weapon")
    print("eat victual")
    print( "attack")
    print("flee")
    print "-" * 30


def start():
    h = Action()
    h.name = raw_input("What is your character's name?\n>")
    print "-" * 60
    print "-" * 60
    print """\t\tWelcome %s, to.....\n""" % h.name
    print """\t\tZOMBIE HIGH SCHOOL!\n"""
    print """\tThe scene is a distopian future"""
    print """%s, you are in high school when the twittersphere""" % h.name
    print """is blowing up about a zombie virus in you town!\n""" 
    print """you look next to you and the awkward shy kid is pale,""" 
    print """eyes glazed over, and bloody spittle oozing from his mouth\n\n"""
    print "\tYour move %s!!!\n" %h.name
    print "-" * 60
    print "-" * 60

    print "type 'menu' to get a menu of actions you can take.\n"

    while h.life > 0:
        line = raw_input("> ").lower()
        if 'qu' in line:
            h.quit()
        elif 'men' in line:
            h.menu()
        elif 'tak' in line:
            h.takeweapon()
        elif 'eat' in line:
            h.snack()
        elif 'at' in line:
            h.attack()
        elif 'fl' in line:
            h.run()
        elif 'eat' in lines:
            h.snack()
        else:
            print "Bewildered and confused... try another action"
start()

