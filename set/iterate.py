#Iterating Over a Set

def iterate(new_set):
    for element in new_set:
        print('the elements of my provided set are: {}'.format(element))

# Example set
my_set = {1, 2, 3, 4}
#apply created function onto the decleared set
iterate(my_set)