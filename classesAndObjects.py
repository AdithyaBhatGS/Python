# Solving a problem by creating objects is one of the popular techniques called as "Object Oriented Programming"

# Class->A class is logical entity

# It is user defined type

# It will not occupy memory

# Through class we can create objects and initialize them

# A class is a template

# We can achieve encapsulation by combining data members and member functions into a single unit called 'class'

# Syntax:

# class class_name(parent_class1,...parent_class n):
    # class_member
    # mem_function1()...

# __init__() ->Constructor in python

# self -> points to current object's/instance's data member

# id(self)==id(object)

# self -> represents the current object

# Objects->Instance of a class is known as objects

# Can create any number of objects of a class 

#It is also called a 'Physical entity' because it occupies memory 

# By calling 'Constructor' an object can be instantized 
i=1
class Parrot():
    species='bird'

    def __init__(self,name,age,weight):
        self.name=name 
        self.age=age 
        self.weight=weight 

    def print_details(self):
        global i
        print(f"Bird {i} details are : ")
        print(f"Name:{self.name}\nAge:{self.age}\nWeight:{self.weight}\nSpecie:{Parrot.species}")
        i+=1
# Instantizing objects

# Here Parrot(value1,value2,value3) is parameterized constructor that takes 3 arguments or parameters

# Syntax: obj_name=class_name(parameters)

parrot1=Parrot('aranya',5,8)
parrot2=Parrot('amartya',7.5,10)

#calling a method
# Syntax: obj_name.method() 
parrot1.print_details()
parrot2.print_details()

