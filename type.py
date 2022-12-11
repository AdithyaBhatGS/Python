# type(object_name)->It will basically return the type of the object that we pass into the function

def type_checker(a,b,c,d,e):
    print(f"datatype of a:{type(a)}")
    print(f"datatype of b:{type(b)}")
    print(f"datatype of c:{type(c)}")
    print(f"datatype of d:{type(d)}")
    print(f"datatype of e:{type(e)}")
# a,b,c,d,e->objects
a=10
b=22.33
c=None
d=False 
e="aMITH"

type_checker(a, b, c, d, e)