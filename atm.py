data = [
            ['names','account_no','balance'],
            ['Amrita','ac12345', 20000],
            ['Srividya','ab54321', 90000],
            ['RBI','b123456', 0]
]


def balanceEnquiry(id):
    for i in data: 
        
        if i[1] == id:
            print("Your current balance is: " + str(i[2]))

def cashwithdrawal(id): 
    a = int(input("Enter the withdrawal amount: "))
    for i in data: 
        
        if i[1] == id:
            
            newbalance = i[2]-a  
       
    print("Your current balance is "+ str(newbalance))

def cashdeposit(id): 
    a = int(input("Enter the deposit amount: "))
    for i in data: 
        
        if i[1] == id:
            
            newbalance = i[2]+a  
       
    print("Your current balance is "+ str(newbalance))


id = input("Enter your ID: ")


print("Press 1 for cash withdrawal")
print("Press 2 for cash deposit")
print("Press 3 for balance enquiry")

b = int(input("Press the required number accordingly: "))


if b == 1:
    cashwithdrawal(id)

elif b == 2:
    cashdeposit(id)

elif b == 3:
    balanceEnquiry(id)




