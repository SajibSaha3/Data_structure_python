#Accessing Dictionary Values

# Example dictionary
my_dict = {'name': 'Sajib', 'age': 26, 'city': 'Dhaka'}

# Accessing values using keys
name = my_dict['name']
age = my_dict.get('age')
city = my_dict["city"]

# Printing accessed values
print('my name is :', name)
print('my age is:{}'.format(age))
print(f"My City name is :{city}")