# See : https://www.python.org/dev/peps/pep-0008/ 
# for best practices

# This covers lessons 1 and 2

print(6 ** 9)

# div
print(10 // 3)

# use snake case for variable names e.g
my_var = 123 / 25
print(my_var)

my_other_var = 5e9 * .06
print(my_other_var)

# python works with floats by default

# we can determine the type of a variable

print(type(my_var))

# python truncates on conversion
my_other_var = int(my_other_var + 0.543)
print(type(my_other_var))
print(my_other_var)

# use a max of 80 chars per line (though 99 may sometimes be acceptable)

# let's get an exception in the house

print(5/0)

# obligatory line

print("\"Hello world!\" is \'cool\'.")

# more stringy stuff

print(len('hello' + "world"))

print('The length of ' + 'hello' * 5 + ' is: ' + str(len('hello' * 5)) + '.')

my_converted_int = int('420')
print(my_converted_int)

my_str = "I got {} problems but {} ain't one!".format(99, 3.14)
print(my_str)

print(my_str.split(None,3))