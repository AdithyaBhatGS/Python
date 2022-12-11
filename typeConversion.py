# str(),int(),float() are the functions used to convert the data items to string,int,float respectively


print(f"{int('99')} is of the type:{type(int('99'))}")

a=100
print(f"{str(a)}")
print(f"{type(str(a))}")

b=99.99
print(int(b))
b=str(b)
print(type(b))

c=12

c=float(12)
print(c)
print(type(c))

print(42==42.0)
print(42=='42.0')