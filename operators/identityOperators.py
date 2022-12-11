#They are used to check if two variables are pointing to same memory location

#"is" and "not is"
#"not is" works reverse of "is"
a="Ram"
b=a

if(b is a):
    print("Both a and b points to same object!")
else:
    print("a and b points to different object!")
print(f"Address of a:{id(a)}")
print(f"Address of b:{id(b)}")
print("---------------------")
c="Ram"
d="Raju" 

if(d is c):
    print("Both c and d points to same object!")
else:
    print("c and d points to different object!")

print(f"Address of c:{id(c)}")
print(f"Address of d:{id(d)}")

a='Ram'

b='Ram'

print(a==b)

print(b is a)