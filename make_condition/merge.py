#Dictionary Merging with Comprehension


# Example dictionaries
#dict1 = {'a': 1, 'b': 2, 'c': 3}
#dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merging and modifying values
#merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
#print('Merged and Modified Dictionary:', merged_dict)

def merge(dic_1, dic_2):
    union = set(dic_1) | set(dic_2)

    filter_dic={}
    for key in union:
        key_1= dic_1.get(key,0)
        key_2= dic_2.get(key,0)
        filter_dic[key]= key_1 + key_2
    return filter_dic

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

merged= merge(dict1,dict2)
print(merged)
