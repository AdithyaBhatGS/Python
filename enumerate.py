# enumerate(iterables) will add a counter to the iterables where 
# iterables=strings/lists/dictionaries/tuples

list1=['amith','ashok','ankita','sumanth','raghavendra','ram','sita']

# for i,j in enumerate(list1):
    # print(i,end=',')
    # print(j) 
# or
# enumerate()-> adds a counter to each elements in iterables and returns an enumerating object
# list(enum_obj)->list of tuples with each tuple inside the list containing an iterable and a value

obj1=enumerate(list1)
print(list(obj1))

str1='Ashika'
obj2=enumerate(str1)
print(list(obj2))

# for i,j in enumerate(str1):
    # print(i,end=',')
    # print(j)
# 
dict1={'Dosa':'3qty','Idly':'5qty','Pav Bhaji':'3qty'}

obj3=enumerate(dict1)
print(list(obj3))

# for i,j in enumerate(dict1.items()):
    # print(i,end=',')
    # print(j[0],end=',')
    # print(j[1])