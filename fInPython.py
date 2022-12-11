#"f" is a string formatting mechanism in python through which one can improve code readability and reduce the errors

#"f"->When a string is prefixed with "f" all the contents inside "{}" will be treated as value or a variable


name=input("Enter the name : ")
age=int(input("Enter the age : "))

#In the below code {name} will be #treated as variable not a string
#same can be applies to {age}

print(f"Hello {name}!Your are {age} years old!")
print()
print(f"{20*5}")
print()
print(f"{200-29}")