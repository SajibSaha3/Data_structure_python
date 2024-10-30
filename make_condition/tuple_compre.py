#Tuple Comprehension using Generator Expression
'''
n = int(input("enter any number to give a range from 1 to n"))
# Example range of numbers
numbers = range(1, n)

# Creating a tuple of squares of even numbers
even_squares = tuple(x**2 for x in numbers if x % 2 == 0)
print('Tuple of Even Squares:', even_squares) 

'''
# for having odd numbers 
n = int(input("Enter any number to give a range from 1 to n: "))
new_tup = []

for i in range(1, n + 1):  
    i = i ** 3  
    new_tup.append(i) 

# Convert the list to a tuple
new_tup = tuple(new_tup)
print("my new tuple is :--",new_tup)

