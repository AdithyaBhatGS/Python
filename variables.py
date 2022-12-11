'''Variables:
*Name given to address or memory location is called as a variable

*Datatype:Type of the data a memory will hold

*But as we know that everything in Python is treated as objects,a variable is an object whereas datatype of that variable will be class

*Variables->Objects 
*Datatype->Class

Note:Python is a dynamically typed language

Means there is no need of declaring the type of the variable or the variable itself before using it.

You can declare and assign value at same time
'''

a=10
b=22.22
c="Hello"

print("Before : ")
print(f"Value in a:{a} Type of a:{type(a)}")
print(f"Value in b:{b} Type of b:{type(b)}")
print(f"Value in c:{c} Type of c:{type(c)}")

a=c 
c=b 

print("After : ")
print(f"Value in a:{a} Type of a:{type(a)}")
print(f"Value in b:{b} Type of b:{type(b)}")
print(f"Value in c:{c} Type of c:{type(c)}")

# Assigning a value to multiple variables ins 1 line

num1=num2=num3=0


