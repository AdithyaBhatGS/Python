# Logical operators on the basis of logic returns a boolean value
# 
# and,or,not 
# 
# and-> True and True=True 
    #   else False 
# or->False or False=False 
    #   else True 
# not-> not(True)=False 
    #   not(False)=True 

#Truth table for or operator

print("-------------------")

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Truth table for not operator

print("-------------------")

print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Truth table for not operator

print("-------------------")

print(not(True))
print(not(False))

print("-------------------")

print(10>3 and 3<5)
print(10>3 and 11<2)
print(100>33 or 100>1000)
print(100>1000 or 1000<1)
print(not not not True)
print(not not not not False)



