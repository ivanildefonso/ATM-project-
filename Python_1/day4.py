# CLI application that keeps a record of animals I own
# Animal types: Animal, Cat, Dog
#           - Attributes: Name, Age
# Want to store our animal information to a file
# Upon restarting application, want to load animal data from file

# Importing animal module
import animal
import re

#create function to interact with command line 
#used to create animal object from user -inputed values
def add_animal():
    while True:
        try:
            print('Hello! please select type of animal to input')
            print("\t a) Generic animal")
            print("\t c) Cat")
            print("\t d) Dog")
            typeAnimal = input(">>>")

        #input verification
            if not typeAnimal == "c" and not typeAnimal == 'd' and not typeAnimal == 'a':
                raise ValueError('Invalid input for animal type')
            else:
                break
        except ValueError:
            print("oh no! please eneter a valid type for animal: ('a', 'c', 'd')")
    
    while True:        
        try:
            print('\n\nEnter animal name:')
            name = input('>>>')
            break
        except ValueError:
            print('Oh no! please enter a nane using words: (A-Z)')

    while True:    
        try:
            print('\n\nEnter animal age:')
            age = int(input('>>>'))
            break
        except ValueError:
            print("Oh no! You must enter a number for the age: Try again")


    if typeAnimal == 'a ':
        newAnimal = animal.Animal(name, age)
    elif typeAnimal == 'c':
        newAnimal= animal.Cat(name, age)
    else: 
        newAnimal = animal.Dog(name, age)

    return newAnimal

print(add_animal())

#open and saving lst_animals in text file
def save_animals(lst_Animals):
    f = open ('saved_animals.txt', 'w')

    for animal in lst_Animals:
        f.write(animal.name + ',' + str(animal.age) + ',' + animal.animal_type + '\n')
    f.close()

#load animals from saved_animals.txt
def load_animals():
    f = open('saved_aninal.txt', 'r')
    lst_animals = []
    for line in f: 
        if line == '':
            break
        animal_data = line.slip(',')
        if animal_data [2].strip() == 'Generic':
            newAnimal = animal.Animal(animal_data[0], animal_data[1])
        elif animal_data[2].strip() == 'Cat':
            newAnimal= animal.Cat(animal_data[0], animal_data[1])
        else: 
            newAnimal = animal.Dog(animal_data[0], animal_data[1])
        
        lst_animals.append(newAnimal)
    return lst_animals

#Main Function
#Important! Main will loop to begin the application
def main():
    print('Welcome to the Animal Journal')

    lst_Animals = load_animals()
#create infinte loop
    while True:
        try:
            print('Please select an option:')
            print('\ta) add new Animal')
            print('\tq) Quit')

            option = input('>>>')

            if option =='q':
                break #break infinite loop
            elif option == 'a':
                lst_Animals.append(add_animal())
                #complete task
            else:
                raise ValueError('Invalid menu option')
        except ValueError:
            print('invalid option: Please try again!')
        
    #breaking from loop
    for animal in lst_Animals:
        print(animal, type(animal))

if __name__ == '__main__':
    main()


print(add_animal)

#crate file on terminal
#myFile = open('file1.txt', 'w') or 'r' for reading or 'a' for append
#write = myFile.write('This line goes at the end!')




