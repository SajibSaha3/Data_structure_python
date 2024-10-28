# List comprehension is a concise way to create lists using an expression and iteration.

# Creating a list of cubing of numbers from 0 to n
n= int(input())
cubed_list = [x**3 for x in range(n)]

# Printing the list
print('my created new list is:-- {} which contains the cubed values from 0 to {}'.format(cubed_list,n))