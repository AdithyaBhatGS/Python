#Importing modules calculator and greetuser
#Use keyword import

#Shortening module names while importing with "as"

#import calculator as cal

#Now you can use cal.fun_name() or cal.variable instead of calculator.fun_name() or calculator.variable

#If you want to import all the functions or variables form a module then:-

#from module_name import*

#now you don't need to use module_name.fun_name() rather simply use fun_name

#But doing this can result in error if there are two function one in module 1 and another in module 2 and you've imported both

import calculator,greetUser

def fun(a,b):

    #Here we're calling the functions present inside the module "calculator"

    #Syntax: module_name.fun_name()
    #        module_name.var_name

    print(calculator.add(a,b))
    print()
    print(calculator.sub(a,b))
    print()
    print(calculator.mul(a,b))
    print()
    print(calculator.div(a,b))
    print()
    print(calculator.floor_div(a,b))
    print()
    print(calculator.pow(a,b))
    print()

name=input("Enter your name!")

#We're calling the greet fun of module greetUser

greetUser.greet(name)
a=int(input("Enter value 1"))
b=int(input("Enter value 2"))
fun(a,b)
