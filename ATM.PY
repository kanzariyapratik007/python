#ATM
balance=2000
print ("""

welcome to a atm machine
choice transaction
             
1)BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT
""")
p1= int(input("enter  transaction"))#option = int(input("Enter Transaction "))
if (p1==1):
    print ("your balance",balance)
elif (p1==2):
    withdraw=int(input("Enter amount to withdraw "))
    if(balance > withdraw):
        total=balance-withdraw
        print ("success")
        print ("your new balance",total)
    else:
        print ("no balance")
elif (p1==3):
    deposit=int(input("enter a depoisit"))
    totalbalance=balance+deposit
    print ("success") 
    print ("new amout",totalbalance)  
elif(p1==4):
    exit("sorry")
    
else:
    print ("sorry")        



    
         
           



