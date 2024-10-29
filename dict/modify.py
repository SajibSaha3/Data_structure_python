#Modifying Dictionary Values
#initialize a function
def replace(new_dic):
    #access the dict elements by extract key and value 
    for key,value in new_dic.items():
        #update the value of age with new value
        if value==26:
            new_dic[key] = 40


# Example dictionary and apply decleared function into this 
my_dict = {'name': 'Sajib', 'age': 26}
replace(my_dict)
#print the updated dictionary 
print('my updated dict is : {}'.format(my_dict))
