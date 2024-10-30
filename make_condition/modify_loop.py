new_dic = {
    'persons': {
        'name': ['sajib', 'khan'],
        'details': {
            'age': [26, 22],
            'city': ['dhaka', 'khulna'],
            'skill': {
                'program': ['python', 'java'],
                'web': ['react', 'django']
            }
        }
    }
}

for key, value in new_dic.items():  
    if key == 'persons':  
        for person_key, person_value in value.items():  
            print(f"{person_key}: {person_value}") 

            # If person_key is 'details', iterate through its contents
            if person_key == 'details':
                for detail_key, detail_value in person_value.items():
                    print(f"  {detail_key}: {detail_value}")  # Print details