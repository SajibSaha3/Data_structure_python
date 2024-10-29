#Checking Membership in a Dictionary

def check(dict):
    for key, value in dict.items():
        if value=="sajib":
            print('value "Sajib" exists in the dictionary')
            break
    else:
        print('value "Sajib" does not exist in the dictionary')
   
# Example dictionary
new_dic = {'name': 'Sajib', 'age': 26 }

check(new_dic)


