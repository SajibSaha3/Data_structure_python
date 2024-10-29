#Tuple Comprehension (using generator expression)

n = int(input("Give the range you want : "))

# Creating a tuple of cube of numbers from 0 to n
squared_tuple = tuple(x**3 for x in range(n))

# Printing the tuple
print('the cubed value for your given range are : {}'.format(squared_tuple))