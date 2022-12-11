class ATM():
    def __init__(self):
        self.pin=''
        self.balance=0

        self.menu()
    
    def menu(self):
        print("""
            Hello!Welcome to Namma ATM!
            
            Available Services : 
            
            1.Create PIN
            2.Deposit
            3.Withdraw
            4.Check Balance
            5.Reset PIN
            6.Exit
        """)
        choice=int(input('Enter your choice : '))
        if(choice<1 or choice>6):
            print("Invalid user input!")
            menu()
        else:
            if(choice==1):
                self.create_pin()          

            elif(choice==2): 
                self.deposit()
                
            elif(choice==3):
                self.withdraw()

            elif(choice==4):
                self.check_balance()

            elif(choice==5):
                self.reset_pin()

            elif(choice==6):
                self.exit()
    
    def create_pin(self):
        temp=input('Enter the pin to be created : ')
        self.pin=temp 
        print('Pin created successfully!') 
        self.menu()
    
    def deposit(self):
        temp=input('Enter the pin!')
        if(temp==self.pin):
            amt=int(input('Enter the amount to be deposited!'))
            self.balance+=amt
            print(f'{amt} deposited successfully!') 
        elif(self.pin==''):
            print("Account does\'nt exist!")
        else:
            print('Invalid pin entry!')
        self.menu()
    
    def withdraw(self):
        temp=input('Enter the pin!')
        if(temp==self.pin):
            amt=int(input('Enter the amount to be withdrawn!'))
            if(amt<=(self.balance-2500)):
                self.balance-=amt 
                print(f'{amt} withdrawn succesfully!')
            else:
                print('Insufficient Balance!')
        else:
            print('Invalid pin entry!')
        self.menu()

    def check_balance(self):
        temp=input('Enter the pin!')
        if(temp==self.pin):
            print(f'Balance:{self.balance}')
        else:
            print('Invalid pin entry!')
        self.menu()

    def reset_pin(self):
        temp=input('Enter the pin!')
        if(temp==self.pin):
            new_pin=input('Enter the new pin!')
            self.pin=new_pin
            print('Pin successfully updated!')
        else:
            print('Invalid pin entry!')
        self.menu()

    def exit(self):
        temp='thank you for using our service!'
        print(temp.title())
    

sbi_atm=ATM()
# hdfc_atm=ATM()
