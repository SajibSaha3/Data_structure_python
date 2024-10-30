#List Comprehension with Conditional Nesting

'''
# Example matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flattening and filtering even numbers from the matrix
even_flattened = [num for row in matrix for num in row if num % 2 == 0]

print('Flattened Even Numbers:', even_flattened)
'''

def even(new):
    check=[]
    for i in new:
        for j in i:
            if j % 2 == 0:
                check.append(j)
    return check
                
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_res= even(matrix)
print(final_res)


sort_li= [j for i in matrix for j in i if j % 2==1]
print(sort_li)