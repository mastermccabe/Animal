# from animal import Animal
class Animal(object):
    def __init__(self,name,health):
        # self.health = 10           #  run: health decreases by five
        self.name = name
        self.health = health

    def run(self):
        self.health -=5
        return self                 # display health: print to the terminal the animal's health.

    def walk(self):
        self.health -= 1
        return self

    def displayHealth(self):
        print 'health: ',self.health
        print "name: ",self.name
        return self

class Dog(Animal):
    def __init__(self,name,health):
        super(Dog, self).__init__(name,health)    # use super to call the Animal __init__ method
        self.health = 150               # every Ninja starts off with 10 stealth
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name,170)  # use super to call the Animal __init__ method
        # self.health = 170
        # return self           # every Samurai starts off with 10 strength
    def fly(self):
        self.health -= 10
        print 'flying away'
        return self
    def displayHealth(self):
        print 'health:',self.health, 'i am a dragon'

animal1 = Animal("animal1",20)
animal1.displayHealth()
print 'now walking',animal1.name,'three times and running twice'
animal1.walk().walk().walk().run().run().displayHealth()
print "----------- new character ----------- \n"

dog1 = Dog('dog1',1)
dog1.displayHealth()
dog1.walk().walk().walk().run().run().pet().displayHealth()
print "----------- new character ----------- \n"
dragon1 = Dragon("Dragon1")
dragon1.displayHealth()
dragon1.fly().displayHealth()
print "----------- new character ----------- \n"
#Uncomment below
# dog2 = Dog('dog2',1).fly().displayHealth()
# AttributeError: 'Dog' object has no attribute 'fly'
