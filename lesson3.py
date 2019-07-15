# Data structures

# Lists
# We can create lists of objects of various types
# Indexing is 0 based but we've got Matlab style slices

my_list = ['stuff', 3.14, 'LLama', 25]

print(my_list[1:2])

# We can also index from the end of the list

print(my_list[-3])

print(my_list[2:])

# Membership operators
print('LLama' in my_list)

print(42 not in my_list)

# Strings are NOT mutable

my_str = "Alberto"
print(my_str[0])

# Error
# my_str[0] = 'B'

# We can sort lists of objects of the same type (unsurprisingly so)

my_list = [4, 3, 2, 1, 0]
my_list.append(25)
my_sorted_list = sorted(my_list)
print(my_sorted_list)

my_str_list = ["How", "are", "you"]
sentence = ' '.join(my_str_list)
sentence += '?'
print(sentence)

# Tuples, like Lists but immutable
# They can also be sliced

pos_main = 25.32, 43.31, -32.54
speed = (10, 10, 0) # with or without parantheses
new_pos = pos_main + speed
# not what you'd expect, this actually concatenates the tuples
# which makes sense since they are immutable
print(new_pos)

# Sets (like Math sets)
# Unordered, mutable, unique

my_list.append(25)
my_set = set(my_list)
my_set.add(25)
my_set.add(25)
print(my_set)
my_set.pop()

# Dictionaries (i.e. Maps)
# Unordered, mutable, unique, immutable key
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}


# Identity operators
# 'is', 'is not'

au_exists = elements.get('aurum') is not None
print(au_exists)

# get() is safer than [] obv
print(elements['helium'])

# Identity vs equality

'''
List a and list b are equal and identical. 
List c is equal to a (and b for that matter) since they have the same contents. 
But a and c (and b for that matter, again) point to two different objects, i.e., t
hey aren't identical objects. 
That is the difference between checking for equality vs. identity.
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

# Compound data structures (dict of dict)
elements = {'hydrogen': 
                {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas' : True},
            'helium': 
                {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas' : False}
            }

print(elements['helium']['is_noble_gas'])

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
verse = verse.split()
print(verse)
unique_words = set(verse)
print(len(unique_words))