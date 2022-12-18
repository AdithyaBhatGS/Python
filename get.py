dict1={1:'Bengaluru',2:'Mysuru',3:'Manglore',4:'Kolar',5:'Belgavi'}

# get(x,y) -> Method takes two parameters 

# x->key name whose value to be checked

# y->if value doesn't exist the what should be returned 

# y is optional if not specified then it returns None if value doesn't exist

print(dict1.get(4,0))

print(dict1.get(11,0))