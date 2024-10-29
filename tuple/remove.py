#Removing Elements from a Tuple


# Example tuple
my_tuple = (1, 2, 3, 4,5)

# Converting to a list and removing an element
temp_list = list(my_tuple)
del temp_list[1:3]
my_tuple = tuple(temp_list)

# Printing the tuple after removal
print('Tuple after Removal:', my_tuple)