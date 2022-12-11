birthday_list={'Alice': '18 Jan','Bob':'22 May','Willey':
'1 June'}
flag=1
while(flag):
    flag=int(input('Enter 0 to quit!'))
    if flag==0:
        continue
    name=input('Enter the name : ')

    if(name==''):
        print('Name cannot be empty!')
        continue 
    else:
        if name in birthday_list:
            print(f"{birthday_list[name]} is the birthday of {name}!")
        else:
            day=input('Enter the day:')
            birthday_list[name]=day
            print('Birthday database got updated!')
            print(birthday_list)
        