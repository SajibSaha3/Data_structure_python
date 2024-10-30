#  Set Comprehension and  with Condition
# Creating a set using comprehension with a condition to filter specific elements.

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_li =[]
def even(li):
    for element in li:
        if element % 2 == 0:
            even_li.append(element)
    return even_li
new_li= even(numbers)
print('my even list is : {}'.format(new_li))



# Creating a set of even numbers
odd_set = [num for num in numbers if num % 2 == 1]

print('Set of Even Numbers:', odd_set)