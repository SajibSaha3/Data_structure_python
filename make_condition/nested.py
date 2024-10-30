#Dictionary with Nested Structures
# Example dictionary with nested structures
nested_dict = {
    'person': {'name': 'Sajib','details': {'age': 25,'city': 'Dhaka','skills': ['Python', 'Data Analysis']}}
                }

# Accessing nested elements
city = nested_dict['person']['details']['city']

# Modifying a nested element
nested_dict['person']['details']['skills'].append('Machine Learning')

print('City:', city)
print('Updated Nested Dictionary:', nested_dict)