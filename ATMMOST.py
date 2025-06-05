
print ("WELCOME TO ATM")
pin=int(input("enter a pin  :"))
if (pin==101):
    print ("right")
else:
    print ("wrong pin")

import mysql.connector as p

def vish(n):
    
        satish = p.connect(host="localhost", user="root", password="1234", database="atm")
        pratik = satish.cursor()

        
        BALANCE =  2000 
        match n:
            
                

            case 1:
                DEPOSIT = int(input("Enter deposit amount: "))
                BALANCE += DEPOSIT
                print("Deposit successful")
                print("Total balance now is:", BALANCE)
                pratik.execute("INSERT INTO atm1 (BALANCE, DEPOSIT) VALUES (%s, %s)", (BALANCE, DEPOSIT))
                satish.commit()

                
                
                
            case 2:  # Withdraw
                WITHDRAW = float(input("Enter withdraw amount: "))
                if BALANCE >= WITHDRAW:
                    BALANCE -= WITHDRAW
                    print("Withdrawal successful")
                    print("Your new balance is:", BALANCE)
                    pratik.execute("INSERT INTO atm1 (BALANCE,WITHDRAW) VALUES (%s, %s)", (BALANCE,WITHDRAW))

                    satish.commit()
                else:
                    print("Insufficient balance")

            case 3:  # Deposit
                pratik.execute("INSERT INTO atm1 (BALANCE) VALUES (%s)", (BALANCE,))
                satish.commit()
                print("Initial balance recorded successfully",BALANCE)


vimal = int(input("Enter ( 1: Deposit, 2: Withdraw, 3: BALANCE): "))
vish(vimal)
