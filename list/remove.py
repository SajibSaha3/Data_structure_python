#Removing Elements from a List


# Example list
my_list = ['a', 'b', 'c', 'd']

# Removing elements
my_list.remove('c')
#want to remove 'd'as well
popped_item = my_list.pop(-1)

# Printing the list after removal
print('List after Removal:', my_list)
print('Popped Item:', popped_item)