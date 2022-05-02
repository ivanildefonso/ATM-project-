#classes always start with Capital letter
class Animal:
    isAlive = True #class attribute

#class constructor. Built specific objects from class __init__
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age 
    
    def sleep(self): #creating a method
        print('zzz')

    def move(self):
        print(self.name, 'has moved')

    def eat(self):
        print(self.name, 'has gain energy')

#object of type Animal
a1 = Animal('Fred', 5)
a2 = Animal('Stacy', 7)

print(a1)
a1.sleep

print(a1.name)
print(a1.age)
print(a1.isAlive)
a1.sleep()

a1.move()
#Struggled to show on terminal

#childclass
#inherent all methods and properties from parent class
class Cat(Animal):
    def sleep(self): #alter sleep from parent class
        print('brbrbr')
    def move(self):
        print('run')

class Dog(Animal):
    def sleep(self): #alter sleep from parent class
        print('mmmm')
    def move(self):
        print('jump')


d1 = Dog('fredo', 2)
print(d1)


c1 = Cat('bob', 4)
c1.sleep()
print(c1)
