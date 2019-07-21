import math

K_NUM_EL = 5

def median(list):
    median = 0.
    for element in list:
        try:
            median += element
        except:
            median += 0.
    try:
        median /= len(list)
    except ZeroDivisionError:
        print("List was empty")
    
    return median

def sqrt(list):
    new_list = []
    for element in list:
        if element >= 0:
            new_list.append(math.sqrt(element))
    return new_list