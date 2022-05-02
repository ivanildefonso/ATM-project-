# Parent class
class Animal:
    isAlive = True

    # Cunstructor/initializer of object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('*zzz*')

    def move(self):
        print(self.name, "has moved.")

    def eat(self):
        print(self.name, "has gained energy.")

    def __str__(self):
        return self.name + ": " + str(self.age)
        
# Child class of Animal
class Cat(Animal):
    def sleep(self):
        print("*purr*")

    def move(self):
        print(self.name, "has walked.")

# Child class of Animal
class Dog(Animal):
    def sleep(self):
        print("*snore*")

    def move(self):
        print(self.name, "has run.")

a1 = Animal("Fred", 5)
c1 = Cat("Bob", 4)
d1 = Dog("Fido", 2)



# Initializing instances of Animal/Cat/Dog
def main():
    a1 = Animal("Fred", 5)
    c1 = Cat("Bob", 4)
    d1 = Dog("Fido", 2)

    lst_animals = [a1, c1, d1]

    for obj in lst_animals:
        print(obj)
    obj.sleep()
    obj.move()
    obj.eat()
if __name__ == '__main__':
    main()

''''
#Main Method used to transport specific code to another file
#everything in main wont run

def main():

####hidden code###

if __name__ == '__main__':
    main()
'''

