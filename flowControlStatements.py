# Use of if,if-else,elif :

# use of if statement
if(10%2==0):
    print("10 is even!")

# use of if else statement
num=int(input('Enter a number  : '))
if(num%2==0):
    print(f"{num} is even!")
else:
    print(f"{num} is odd!")

#use of elif

num=int(input('Enter a number:'))
if(num>0):
    print(f"{num} is a positive number!")
elif(num<0):
    print(f"{num} is a negative number!")
else:
    print(f"{num} is neither positive nor negative")

