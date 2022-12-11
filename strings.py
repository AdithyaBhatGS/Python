
a="Browny ate 2 biscuits"

print(type(a))

#Different way of representing a string

# a='Hello'

# When you want a single quote in between then use " " 
print("Kitty's chain was snatched by a theif yesterday!")

# a="Hello"

# Multiline strings
# a='''Hello'''
print("-----------------------")
print('''Hello,
    I am Smith,
    I am an avid reader,
    I spend my time reading about buisnesses ,sport and movies''')
print("-----------------------")
# print(a)

#use of len in strings

cpp="Standard template library"
print(len(cpp))
print("-----------------------")

# string slicing
# slicing means getting a part of string

str1="Alice in Wonderland!"

print(str1[len(str1)-1])

print(str1[2:6])

print(str1[5:])

print(str1[:7])

print(str1[:-1])

print("-----------------------")

# Concatenation of strings

print('4'+'6'+'7')

print('Good'+' Morning '+str(int(100)))

print("-----------------------")
#Replication of strings

print('Mathematics '*3)

print("National Stock Exchange\n"*2)

print("-----------------------")

# string functions

# 1)capitalize()
# It will take string object and returns a string object with first letter as an Upper case character

str1='heLLO BuDDy'
print(str1.capitalize())

print("-----------------------")

# 2) isupper()
# Takes string object as an input and returns a boolean value(evaluates wheather all characters in the string is upper case character or not)

str1='hELLO WORLD'
str2='HELLO123'
print(str1.isupper())
print(str2.isupper())

print("-----------------------")

# 3)islower()

#Takes string object as an input and returns a boolean value(evaluates wheather all characters in the string is lower case character or not)

str1='hello world 333'
str2='hellO'
print(str1.islower())

print(str2.islower())

print("-----------------------")

# 4)upper()

# Takes a string object and converts all characters to upper case

print('ID:amith112'.upper())

print('hello world'.upper().isupper())
print("-----------------------")

# 5)lower()

# Takes a string object and converts all characters to lower case

print('HELLO GOOD MORNING!'.lower())
print('HELLO'.lower().islower())

print("-----------------------")

# 6)isX methods
# Includes:isalpha(),isalnum(),isdigit(),isspace(),istitle()

str1='heLLO'
str2='1hello'

print(str1.isalpha())
print(str2.isalpha())

print("-----------------------")

str1='Hello125'
str2='Hello'
str3='123'
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print('123_aaa'.isalpha())
print("-----------------------") 

print('123'.isdigit())
print('123a'.isdigit())
print('aaa'.isdigit())

print("-----------------------")

print('\n\t\n \n \t'.isspace())
print('     .'.isspace())

print("-----------------------")

print('Hello! I Am Ram!'.istitle())
print('Hello! i Am Ram!'.istitle())

print("-----------------------")

# 7)startswith() and endswith()

print('Mathematical Computing in Polymorphical Environment'.startswith('Math'))

print('Mathematical Computing in Polymorphical Environment'.startswith('Mathz'))

print('Mathematical Computing in Polymorphical Environment'.endswith('nt'))

print('Mathematical Computing in Polymorphical Environment'.endswith('nt.'))

print("-----------------------")

# 8)count()

# count() ,counts the occurence of a character or sub string present in the given string object
    
str1='Rama is said to have been born to Kaushalya and Dasharatha in Ayodhya, the ruler of the Kingdom of Kosala. His siblings included Lakshmana, Bharata, and Shatrughna. Ram married Sita. Though born in a royal family, their life is described in the Hindu texts as one challenged by unexpected changes such as an exile into impoverished and difficult circumstances, ethical questions and moral dilemmas'

print(str1.count('a'))
print(str1.count('Ram'))

print("-----------------------")

# 9)find() 

# find() returns the index of the first occurence of a character or substring ,if its not present then it returns -1
str1="Ayodhya is a city situated on the banks of holy river Saryu in the Indian state of Uttar Pradesh.Ayodhya is the administrative headquarters of the Faizabad district as well as the Faizabad division of Uttar Pradesh, India." 

print(str1.find('Ayodhya'))

print(str1.find('Uttar Pradesh'))

print(str1.find('z'))

print(str1.find('Z'))

print("-----------------------")

# 10)replace()

# Takes two parameters i.e.
# 'old_string' and 'new_string' and replaces the 'old_string' with 'new_string'

str1='Hello  .How  are    you Charlie!'
print("Before replcaing : "+str1)
print(len(str1))

# If you just use str1.replace('  ',' ') then you're trying to manipulate the exisiting string which is not possible

#When you do str1=str1.replace('  ',' ') the replace() will return a new string to str1 ,hence now str1 holds new object/data item

str1=str1.replace('  ',' ')

print("After replcaing : "+str1)
print(len(str1))

print("-----------------------")

# 11)join(),split()

# join() takes a list and returns a string object


print(' '.join(['Hello','Ramesh!','How','are','you','!']))

print(','.join(['cats','rats','bats','parrots','piegons']))

print("-----------------------")
# split() takes a string and returns a list

list1=("Ayodhya is a city situated on the banks of holy river Saryu in the Indian state of Uttar Pradesh.Ayodhya is the administrative headquarters of the Faizabad district as well as the Faizabad division of Uttar Pradesh, India."
.split(" "))

print(list1)

print(type(list1))

print("-----------------------")