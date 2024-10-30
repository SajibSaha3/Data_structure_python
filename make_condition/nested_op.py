#Nested Lists Operations
'''///
# Example nested list
nested_list = [[1, 2, 3], [4, 5, [6, 7]], [8, 9]]

# Accessing a nested element
nested_element = nested_list[2][1] 

# Modifying a nested element
nested_list[2][1] = 7  # Changing 9 to 10

# Flattening the nested list
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item, list) else [item])]

print('Nested Element:', nested_element)
print('Modified Nested List:', nested_list)
print('Flattened List:', flattened_list) ///'''

nested_list = [[1, 2, 3], [4, 5, [6, 7]], [8, 9],[2,8,12]]
#accessing value 12
find = nested_list[3][2]

#change the value 7 to 6
nested_list[1][2][1] = 6

print('Find {} from the given nested list: '.format(find))
print('after replaced the value "7" is now convert to:  "6"',nested_list)

# now flaten the list
flaten_list = []
final_list= []
for row in nested_list:
    #print(row)
    for number in row:
        if isinstance(number,list):
            for other_num in number:
                flaten_list.append(other_num)
        else:
            flaten_list.append(number)
print(flaten_list)

            

