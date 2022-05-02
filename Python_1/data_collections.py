#data collections

#List-ordered, changeable, duplicates are allowed

test_scores = [90, 85, 79, 65, 92]
for i in range (len(test_scores)):
    print('student at index', i, 'scored an', test_scores[i], 'on the test')


#set-unordered, unchangeable, curly braces{}

new_set = {'apple', 'banana', 'cherry'}
new_set2 = {'tomato', 'orange'}

new_set.union(new_set2) #combine set statements
print(new_set)

#Tuple- collection that is ordered but unchangeable 
#stores multiple items in a single variable, such as list and set
# round brakets  = ()

new_tuple = (1, 3.5, 'hello')
print(new_tuple)

#index tuple
new_tuple[0]

#Dictonary- stores key-value pairs
#ordered, changeable, no duplicates in term of keys 
#Curly brackets = {:}
new_dict = {1:'Fred', 2:'Stacy', 3:'bob'}
print(new_dict)

new_dict[2]

new_dict[4] = 'Maria' #adding to dict
print(new_dict)
