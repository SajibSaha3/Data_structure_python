#Accessing Tuple Elements

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements using positive and negative indices
second_element = my_tuple[1]
last_element = my_tuple[-1]

#Access through slicing 
mul_element = my_tuple[1:3]
# Printing accessed elements
print('Second Element is: {}, Last Element is: {}, and slicing in a specified range is: {}'.format(second_element, last_element, mul_element))
