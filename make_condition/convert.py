# Example 5: List of Tuples to Dictionary
'''
# Example list of tuples
tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Converting to a dictionary
result_dict = {key: value for key, value in tuple_list}

print('Dictionary from List of Tuples:', result_dict)

tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
new_dic = {}
for key, value in tuple_list:

    #print(value)
    new_dic [key]= value
print(new_dic)
'''  

def generate_dic(tup):
    generated_dic = {}
    for key , value in tup:
        generated_dic [key] = value
    return generated_dic

tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
new_dic = generate_dic(tuple_list)
print(new_dic)


