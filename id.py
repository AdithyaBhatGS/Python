# In python "id" will be assigned whenever you create an object
# 
# Each object has its own unique id
# 
# Every time you run the program the id values might change
# 
# id represents the memory address of the object

num1=10

num2=100 

print(id(num1))
print(id(num2))

list1=[10,"female","money",None,True]
print(id(list1))

str1="Ram"
str2="Ram"

if(id(str1)==id(str2)):
    print("Pointing to same memory")
else:
    print("Pointing to different memory")

x=10.22
y=x
print(id(x)==id(y))