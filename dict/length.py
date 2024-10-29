#Dictionary Length
#defining a fuction to count the length of index value 
def length(new_dic):
    #initialize a counter with 0 value as indexd begin from 0 in python as well
    count =0
    #iterate over the dictionary items and count as wll 
    for i in new_dic.items():
        #increase counter value for every iteration
        count += 1
    print("the count of the length of index is: {}".format(count))
    
# Example dictionary
new_dict = {'name': 'Sajib', 'age': 26, 'city': 'dhaka'}

#Apply the decleared function over the dictionary
length(new_dict)