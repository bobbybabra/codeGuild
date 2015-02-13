imort random

class Character:
    def __init__(self):
        self.name = ""
	self.health = health
    def inflict(self, zombie):
	inflict = min(max(randint(0, self.health)- randomint(0, zombie.health), 0), zombie.health)
	zombie.health -= damage
	if inflict == 0:
	    print ("..like a nimble sloth, %s evades %s's attack." % (zombie.name, self.name)
	else
	    print("%s inflicts debilitating damage on %s!!" %(self.name, zombie.name) 
	return zombie.health <= 0

class Zombie(Character):
    def __init__(self, player):
	Character.__init__(self)
	self.name = "a zombie"
	self.health = randomint(1, player.health)
# random_adjective = random['wretched', 'filthy', 'disgusting', 'oozing']

class Player(Character):
    def __init__(self):
	Character.__init__(self)
	self.level = 'normal'
	self.health = 10
	self.health_max = 10
    def quit(self):
	print ("The zombie virus has infected %s. You are now undead and crave brains.") %self.name
	self.health= 0
    def help(self): 
	print Commands.keys()
    def status(self):
	print ("%s's health: %d/%d" %(self.name, self.health, self.health_max)
    def weak(self):
	print ("%s is cold, hungry and tired.") %self.name
	self.health = max(1, self.health -1)
    def rest(self):
	if self.state != 'normal':
	    print ("keep moving %s, zombies coming in hot!") % self.name
	    self.zombie_attack()
	else:
	    print "%s takes a breather." self.name
	        if randint(0,1):
		    self.zombie = Zombie(self)
		    print ("Look out %s! -%s appears!") %(self.name self.zombie_name)
		    self.state = 'fight'
		    self.zombie_attacks()
		else:
		    if self.health < self.health_max:
			self.health = self.health + 1
		    else: print ("%s rested too long.") %self.name
			self.health -= 1
    def ambush(self):
	if self.state != 'normal':
	    print ("%s is too lazy!") % self.name
	    self.enemy_attacks()
##### clean up past here
        else:
            print "%s runs into the book stacks in the library" % self.name
            if randint(0, 1):
            self.zombie = Zombie(self)
            print "%s encounters %s!" % (self.name, self.zombie.name)
            self.state = 'fight'
         else:
            if randint(0, 1): self.tired()
    def flee(self):
        if self.state != 'fight': print "%s runs down a corridor" % self.name; self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.zombie.health):
            print "%s flees from %s." % (self.name, self.zombie.name)
            self.zombie = None
            self.state = 'normal'
        else: print "%s couldn't escape from %s!" % (self.name, self.zombie.name); self.zombie_attacks()
    def attack(self):
        if self.state != 'fight': print "%s flails in the air like a twit." % self.name; self.tired()
        else:
            if self.do_damage(self.zombie):
            print ("%s decapitates %s!") % (self.name, self.zombie.name)
            self.zombie = None
            self.state = 'normal'
        if randint(0, self.health) < 10:
            self.health +=  1
            self.health_max += 1
            print "%s is rejuvinated" % self.name
        else: self.zombie_attacks()
    def zombie_attacks(self):
        if self.zombie.do_damage(self): print "%s's brains were devoured  by %s!!!\nyou are undead and crave BRAINS!!/nunless you're a veggetarian then seek GRAINS!!" %(self.name, self.zombie.name)
 
Commands = {
    'quit': Player.quit,
    'help': Player.help,
    'status': Player.status,
    'rest': Player.rest,
    'explore': Player.explore,
    'flee': Player.flee,
    'attack': Player.attack,
     }
 
p = Player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print """When %s leaves homeroom, they 
a strange stench in the air
	maybe we are disecting a pig in biology today...""" % p.name
 
while(p.health > 0):
    line = raw_input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
    for c in Commands.keys():
        if args[0] == c[:len(args[0])]:
            Commands[c](p)
            commandFound = True
            break
        if not commandFound:
        print "%s is confused, enter a command" % p.name

