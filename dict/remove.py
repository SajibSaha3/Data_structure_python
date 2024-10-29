# Removing Key-Value Pairs from a Dictionary

def remove(new_dic):
    if "age" in new_dic:
        del new_dic["age"]  # Remove the key "age"

    print('New dict after removing the key and value: {}'.format(new_dic))

# Example dictionary
my_dict = {'name': 'Sajib', 'age': 26, 'city': 'Dhaka'}
remove(my_dict)

print('Dictionary after Removal:', my_dict)
