# We have while and for loops in python

# An infinite while loop
# while(True):
    # print("1")

for i in range(10):
    print(i,end=' ')
print("\n------------------------")

for i in range(0,12):
    print(i,end=' ')
print("\n------------------------")

for i in range(0,12,3):
    print(i,end=' ')
print("\n------------------------")

# There are 2 methods to iterate a list

# Method1(without using range):
list1=[10,20,33,99,110]

for i in list1:
    print(i,end=' ')

print("\n------------------------")
# Method2(with using range):
for i in range(len(list1)):
    print(i,end=' ')

print("\n------------------------")

# Iterating through while loop

vegetables=['Brinjal','Cucumber','Carrot','Peas','Cabbage','Cauliflower','Potato','Tomato']

i=0

while(i<len(vegetables)):
    print(vegetables[i],end=' ')
    i+=1