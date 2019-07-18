# Lesson 5 
# Functions

# Simple factorial

# we've also got default arguments
def factorial(n = 1):
    """Return the factorial of a number n"""
    
    if n == 0:
        return 1

    k = 1
    for i in range(n):
        k*=i+1
    return k

num_terms = 8
for i in range(num_terms):
    print("{}! = {}".format(i, factorial(i)))

# Lambdas

fact_m = lambda x : factorial(x) / sum(range(factorial(1), factorial(x)))
print(fact_m(10))

# map()
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

mean = lambda num_list : sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# filter()
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short = lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)