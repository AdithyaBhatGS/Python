# Rules :
# 
# 1)A variable in the global scope is a global variable
# 2)A variable in a function with keyword global is a global variable
# 3)if the variable is used in an assignment statement in the 
# function, it is a local variable
# 4)But if the variable is not used in an assignment statement, it is a global variable

# In python we cannot use same name for a global and local and use it in same scope

# Means we can use same name called 'eggs' in global scope and in local scope but we cannot use global 'eggs' and 'eggs'(local) in the function at same time ,either we should use global 'eggs' or 'eggs'(local)

def fun():
    # Here eggs is a global variable because no assignment statement
    # is used
    print(eggs)
eggs='global'
fun()

print("-----------------------")

# def fun1():
    # print(eggs)
    # results in "referenced before assignment error"
    # Because we're using an assignment statement which means eggs is not a global variable
    # So a variable cannot be printed before it is assigned with a value
    # Here eggs is a local variable
    # eggs='local'
# eggs='global'
# fun1()


def fun2():
    global eggs 
    # Once we use global keyword then it will be a global variable and 
    # now we can update its value
    eggs='spam'
eggs='global'
fun2()
print(eggs)

print("-----------------------")

def fun3():
    eggs='local'
    print(eggs)

eggs='global'
fun3()
print(eggs)