# A list hold multiple objects of similar/different types

# Creating a list

list_of_cities=['Bengaluru','Mysuru','Kanpur','Delhi','Mumbai']

# Printing the created list to console 

print(list_of_cities)

print("-----------------------")

#Finding the length

length_of_list=len(list_of_cities)
print(length_of_list)

print("-----------------------")

# Accessing individual elements of the list

list_of_subjects=['Math','Buisness','History','Kannada']

print(list_of_subjects[-1])
print(list_of_subjects[2])

# If we try to access something outside the valid range we get index out of range error

# print(list_of_subjects[100])
list_of_lists=[['Hello','World'],['cats','rats','rabbits']]

print(list_of_lists[0])
print(list_of_lists[1][1])

print("-----------------------")

# Slicing the list

list_of_nums=[10,12,19,77,88,55,66]

print(list_of_nums[:])

print(list_of_nums[3:])

print(list_of_nums[:3])

print(list_of_nums[2:5])

print(list_of_nums[-3:-1])

print(list_of_nums[:-1])

print("-----------------------")

# Updating the contents of the lists

list_of_odd_num=[1,3,5,6]

print(f"Before update : {list_of_odd_num}")

list_of_odd_num[-1]=7

print(f"After update : {list_of_odd_num}")

print("-----------------------")

# List concatenation and replication

list1=[10,20,30]

list2=[40,55,90]

list1=list1+list2

print(list1)

list1=[1,11,123]*3

print(list1)

print("-----------------------")

# in and not in 

list_of_subjects=['Math','Buisness','History','Kannada']

print('Math' in list_of_subjects)

print('Math' not in list_of_subjects)

print('Biology' in list_of_subjects)

print("-----------------------")

# Removing an element using del

# Whenever we know the value in an index we can use del to delete

list1=['Splendor','Activa','Access','Platina']

del list1[-1]

print(list1)

del list1[0]

print(list1)

print("-----------------------")

#Sorting the list using sort()

list1=[11,99,110,1,-1,-8,-77]

print(f"Before Sorting : {list1}")

list1.sort()

print(f"After Sorting : {list1}")

print(f"Sorting in descending order : ")
list1.sort(reverse=True)
print(list1)
print("-----------------------")

# Inserting an element at the end of the list

list1=[]

captain='Sudarshan'
father='Ram'
mother='Sita'
sister='Vaishnavi'

list1.append(father)
list1.append(mother)
list1.append(sister)
list1.append(captain)

print(list1)

print("-----------------------")

# Inserting an element at a particular position of the list

list1=['Dabur','Sonu','Shanaya']

print(f'Before inserting : {list1}')

list1.insert(1,'Bhanu')
list1.insert(0,'Radha')

print(f'After inserting : {list1}')

print("-----------------------")

# Index of a 'value' in the given list

list1=['badam','anjoor','kaaju','peanuts','pista','dates']

print(list1.index('anjoor'))

print(list1.index('dates'))

# print(list1.index('grapes'))
# if not present it results in value error

print("-----------------------")

# Removing a data item using remove() method
# When same values are present multiple times,there first occurence will be 
# removed
list1=['badam','anjoor','kaaju','peanuts','pista','dates','badam','dates']

print(f"Before removing : {list1}")
list1.remove('dates')
print(f"After removing the dates : {list1}")
list1.remove('badam')
print(f"After removing the badam : {list1}")

print("-----------------------")

