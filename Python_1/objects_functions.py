#list
Ivan = [1, 2, 3, 4, 5]
Lele = [6, 7, 8, 9, 10]

#append
Ivan.append(10)

#slice 
Ivan[:4]

#add lists
Ivan + Lele

#lenght of list
len(Ivan)

#list within a list 
Cain = [
    [1, 2, 3, 4], [5, 6, 7, 8, 9]]:

#lists are mutuable, changeable, whereas, strings are unchangeable.
#for loops 

range(5)
for i in range (5):
    print(i)

#print out element with range
Ivan = [1, 2, 3, 4, 5]
for elem in Ivan:
    print(elem)

#create own functions using def function
def area_rectangle(l,w):
    return l * w
area_rectangle(4,5)
print (area_rectangle)

#fibonacci sequence using.. for i in range()
#for and return have to be in the same tab place so it loops
def fib(x):
    lst = [0, 1]
    for i in range(x):
        lst.append(lst[-1] + lst[-2])

    return lst 

print (fib(10))

#convering str to int
str = 369
val = int(str) / 3
print(val)

#Build-in namespaces 
print(dir(__builtins__))
#global namespaces
def temp_funct():
    global var
    var = 1

temp_funct()
print(var)

#local namespaces
def temp_funct_2():
    var2 = 5
    pass
temp_funct_2()
#print(var2)
#var2 is local so it will only work inside the function

def temp_funct_3():
    var3 = 5 
    def temp_nested_funct():
        var4 = 3 + var3
#print(var4) # will return error. Outside boundary

#python operators 
#assignment operator 
count = 0
while(True):
    if count == 13:
        break
    count += 1
    print(count)

user_input = int(input('Enter Number'))

if user_input == 5:
    print('5 is a terrible number, please select anothe number')
elif user_input > 5 and user_input < 20:
    print('that is a good number')
else:
    print(user_input)

#Functions = a block of code which only runs when called
#You can pass data, known as parameters, into functions
#And fuction can return data as a result 
def print_hello():
    print('hello world')
    
print_hello()
#function needs to be called for code to run on terminal

#custom str using function
def print_custom(str):
    print(str)
print_custom('hola munndo')

#fidning volume of cube suing return 
def vol_cube(side):
    return side ** 3
vol = vol_cube(5)
#print('volume of cube is', vol)

side = int(input('Enter side lenght of cube: '))
print('volume of cube is', vol_cube(side))