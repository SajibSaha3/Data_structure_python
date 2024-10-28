# Adding elements to an existing list 
# Example list
my_list = [1, 2, 3]

# Adding elements
my_list.append(4)  # Append an element to the list
my_list.insert(1, 'Inserted')  # Insert the element "Inserted" into the 1st index position

# Printing the updated list
print('After appending {0} and inserting {1} in 2nd index position, my provided list is now: {2}'.format(4, 'Inserted', my_list))
