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

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)