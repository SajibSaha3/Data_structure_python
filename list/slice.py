#List Slicing

# Example list
my_list = [10, 20, 30, 40, 50]

# Slicing the list from index 1 to 4 (this includes indices 1, 2, and 3)
sliced_list = my_list[-4:-1]  # This will return [20, 30, 40]
# Slicing the list from index 2 to 4 (this includes indices 2, and 3)
another_list = my_list[2:4]  # This will return [30, 40]
# Slicing the list from index 0 to 2 (this includes indices 0, and 1)
final_list = my_list[:2]      # This will return [10, 20]

# Printing the sliced lists
print('The elements of the "sliced_list" are: {}, the elements of the "another_list" are: {} and the "final_list" is: {}'.format(sliced_list, another_list, final_list))
