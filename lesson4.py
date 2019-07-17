# Control flow (bout dam' time)

#if
result = 0

day = 'tuesday'

if day == 'monday':
    result = 12
elif day == 'tuesday':
    result = 42
else:
    result = 'unknown'

print(result)

# logical operators
# 'and', 'or', 'not'

is_cold = True
is_raining = True
is_monday = False

if is_cold or is_raining:
    print('Get your overcoat')
elif is_monday:
    print('Get the car')

# for loop and range()
my_list = list(range(10))
for i in range(len(my_list)):
    my_list[i] += 42

print(my_list)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

name_dict = {}

# a really useless example but still
for name in names:
    name_dict[name] = name_dict.get(name, 0) + 1

print(name_dict)

# Using dict.items()
# Count the number of fruits in your basket. 

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    for fruit in fruits:
        if key == fruit:
            result += value
print(result)

# while 

# Find the nearest square to a number N

N = 42
k = 1
while (k+1)**2 < N:
    k += 1
print(k*k)

# break and continue

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

idx = 0
while True:     # just so we have an excuse to break
    if len(news_ticker >= 140):
        break
    if idx < len(headlines):
        news_ticker += headlines[idx] + ' '
        idx += 1
news_ticker = news_ticker[:140]
print(news_ticker)
print(len(news_ticker))


# TODO

# zip (combine two lists into a tuple)

num_list = [5, 7, 11, 42, 112]
print(num_list)
cars = ['ford', 'jag', 'lambo', 'lada', 'rolls']

for num, car in zip(num_list, cars):
    print("{} : {}".format(num, car))


letters = ['a', 'b', 'c']
nums = [1, 2, 3]

l = list(zip(letters, nums))
for tupl in l:
    print(tupl)
    print("{}: {}".format(tupl[0], tupl(1)))

letters_copy, nums_copy = zip(*l)

# enumerate

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# List comprehensions

# e.g. get all squares of even numbers up to, but not including 'n'

n = 25
squares = [x**2 for x in range(n) if x % 2 == 0]
print(squares)

# if else conditions
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0] if name[0] < 'S' else 'potato' for name in names]
print(first_names)