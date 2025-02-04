# using map and list() functions

# What is map() function
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax
# map(function, iterables)

# Required. The function to execute for each item
# Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

l = list(map(int, input("Enter Sequence of Number with space separated.. ")))
print(l)

def double(a):
    a = int(a)
    return a * a
s = input("Enter Sequence of Number with space separated... ")
print(list(map(double, s)))

