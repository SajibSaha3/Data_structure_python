#Tuple Length


# Example tuple
new_tuple = (1, 2, 3, 4, 5)
#initialize a counter to count the index value 0 to n
count =0 
#used a for loop to both access the value and index number from the given tuple
for index, number in enumerate(new_tuple):
    #increase the counter value with every iteration to index number
    count += 1
print('your provided length of tuple is :--- {}'.format(index))