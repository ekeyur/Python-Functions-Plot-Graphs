"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def __init__(this):
        this.name
        this.health
        this.power

    def alive(this):
        return this.health

    def print_status(this):
        print "%s has %d health and %d power." % (this.name, this.health, this.power)

    def attack(this,object):
        object.health -= this.power
        this.health -= object.power
        print "%s does %d damage to %s." % (this.name, this.power, object.name)
        print "%s does %d damage to %s." % (object.name, object.power, this.name)
        if object.health <= 0:
            print "The %s is dead." % object.name
        elif this.health <= 0:
            print "%s is dead" % this.name

class Hero(Character):
    def __init__ (this):
        this.health = 15
        this.power = 5
        this.name = "Hero"



class Goblin(Character):
    def __init__ (this):
        this.health = 10
        this.power = 4
        this.name = "Goblin"


#Zombie Character

class Zombie(Character):
    def __init__ (this):
        this.health = 20
        this.power = 6
        this.name = "Zombie"

#     def attack(this,object):
#         hero.health -= zombie.power
#         print "The zombie does %d damage to you." % zombie.power
#         if hero.health <= 0:
#             print "You are dead."
# # hero_health = 10
# power = 5
# goblin_health = 6
# power = 2

hero = Hero()
goblin = Goblin()
zombie = Zombie()

while hero.alive():
#while goblin.goblin_health > 0 and hero.hero_health > 0:x
#    print "You have %d health and %d power." % (hero.hero_health, hero.power)
#    print "The goblin has %d health and %d power." % (goblin.goblin_health, goblin.power)
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "4. fight zombie"
    print "5. zombie attacks hero"
    print "> ",
    input = raw_input()
    if input == "1":

        hero.attack(goblin)
        # Hero attacks goblin
        # goblin.goblin_health -= power
        # print "You do %d damage to the goblin." % power
        # if goblin.goblin_health <= 0:
        #     print "The goblin is dead."
    elif input == "2":
        zombie.power

    elif input == "4":

        hero.attack(zombie)

    elif input == "5":
        zombie.attack(hero)

    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    # if goblin.health > 0:
    #     # Goblin attacks hero
    #     goblin.attack(hero)
        # hero.hero_health -= goblin.power
        # print "The goblin does %d damage to you." % goblin.power
        # if hero.hero_health <= 0:
        #     print "You are dead."
