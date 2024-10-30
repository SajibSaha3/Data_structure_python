#Tuple Unpacking

# Example tuple
person_info = ('Sajib', 25, 'Dhaka', 'Engineer', 'Single')

# Unpacking tuple into variables
name, age, *other_details = person_info

print('Name:', name)
print('Age:', age)
print('Other Details:', other_details)