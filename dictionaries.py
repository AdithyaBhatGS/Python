# Dictionaries are key-value pairs

# Key->Belongs to a data type
# Value->Belongs to a data type

states_and_capitals={'Karnataka':'Bengaluru','Gujrath':'Gandhinagar','Kerla':'Kochi','Maharashtra':'Mumbai','Tamil Nadu':
'Chennai'}

print(states_and_capitals['Karnataka'])

print(states_and_capitals['Tamil Nadu'])

print("-----------------------")
# Difference between dictionaries and lists

# Note:In a list elements are ordered,so they are equal only when the similiar elements are in order


# But in dictionaries,elements are unordered,so 2 dictionaries with similiar elements but unordered are considered to be equal or same

list1=[10,20,30]

list2=[20,30,10]

print(list1==list2)

dict1={'Mysuru':10,'Bengaluru':20,'Mangaluru':30}

dict2={'Mangaluru':30,'Bengaluru':20,'Mysuru':10}

print(dict1==dict2)

print("-----------------------")

# keys(),values(),items() method in dictionaries

# These methods will return values similiar to lists and they are of the type dict_keys,dict_values,dict_items respectively

states_and_capitals={'Karnataka':'Bengaluru','Gujrath':'Gandhinagar','Kerla':'Kochi','Maharashtra':'Mumbai','Tamil Nadu':
'Chennai'}

print(states_and_capitals.keys())

print(type(states_and_capitals.keys()))

print(states_and_capitals.values())

print(type(states_and_capitals.values()))

print(states_and_capitals.items())

print(type(states_and_capitals.items()))

print("-----------------------")

# Iterating through keys(),values(),items()

for i in dict1.keys():
    print(i)

print("-----------------------")

for i in dict1.values():
    print(i)

print("-----------------------")

for i,j in dict1.items():
    print(f'Key:{i}->Value:{j}')

print("-----------------------")

# Use of in and not in with keys(),values(),items()

dict1={1:'Alice',2:'Valli',3:'Masan',4:'Rajath'}

print(1 in dict1.keys())

print('Valli' in dict1.values())

print((3,'Masan') in dict1.items())

print(99 in dict1.keys())

print("-----------------------")