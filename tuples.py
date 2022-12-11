# Tuples are similiar to lists

# But you can prefer tuples over lists :
# 1)When you don't want the contents to be updated
# 2)Also since they are immutable they are faster than lists

# Creating a tuple:

tuple1=(10,20,30)

# Printing the contents of a tuple:
print(tuple1)

print(type(tuple1))


tuple2=('Hello',)

# tuple2=('Hello')

# This will return the type as string even though we expect it to be a tuple

# Because whenever a tuple contains only 1 value it will be similiar to a string so do this

print(type(tuple2))

# tuple1=(10,20,30,40)
# tuple1[3]=55

# Cannot update the contents like above as it is basically an immutable type