# enumerate(iterables) will add a counter to the iterables where 
# iterables=strings/lists/dictionaries/tuples

list1=['amith','ashok','ankita','sumanth','raghavendra','ram','sita']

for i,j in enumerate(list1):
    print(i,end=',')
    print(j) 

str1='Ashika'

for i,j in enumerate(str1):
    print(i,end=',')
    print(j)

dict1={'Dosa':'3qty','Idly':'5qty','Pav Bhaji':'3qty'}

for i,j in enumerate(dict1.items()):
    print(i,end=',')
    print(j[0],end=',')
    print(j[1])