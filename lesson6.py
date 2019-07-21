# Lesson 6
# Very basic scripting

names = input("Write a list of names: ").title().split(',')
assignments = input("Write the amount of assignments left for each nane: ").split(',')
grades = input("Grade each assignment: ").split(',')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, int(grade), int(grade) \
    + int(assignment) * 2 ))

# Exceptions

try:
    x = int(input("input a number: "))
except: 
    # we can use except for catching a specific set of exception types
    # i.e ValueError and TypeError
    print("Invalid input, please input a number.")
else:
    print("Input was valid.")
finally:
    print("Have a nice day.")


# Example 

def party_planner(cookies, people):
    
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e:
        print("Invalid number of people")
        print(str(e))

    return(num_each, leftovers)

lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")

# Files

# default mode is read-only if unspecified

# using 'with' to auto close file
with open('txt/testFile.txt', 'w') as f:
    f.write("This is a test file.\n")

with open('txt/testFile.txt') as f:
    print(f.read())

# Example

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list

cast_list = create_cast_list('txt/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

# import
# use the name of the file for accessing data inside it

import module.functions1 as fun
import random

test_list = []
for i in range(fun.K_NUM_EL):
    test_list.append(random.gauss(10, 1))
print(test_list)

print(fun.median(test_list))
print(fun.sqrt(test_list))


