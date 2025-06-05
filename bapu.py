import mysql.connector as p

def vish(n):
    
    satish = p.connect(host="localhost", user="root", password="1234", database="atm")
    pratik = satish.cursor()
    


    match n:

        
        case 0:#create database 
            pratik.execute("CREATE DATABASE atm")

            
        case 1:#create a table
            pratik.execute("CREATE TABLE atm1 (eid int, ename VARCHAR(255), DEPOSIT float")

        case 2:# insert
        
        
            eid = int(input("Enter eid: "))
            ename = input("Enter ename: ")
            esel = float(input("Enter esel: "))


            pratik.execute("INSERT INTO student (eid, ename, esel) VALUES (%s, %s, %s)", (eid, ename, esel))
            satish.commit()  



        case 3:#delete
        
    
            shivam= int(input("Enter eid to delete: "))
            pk = "DELETE FROM student WHERE eid = %s"
            pratik.execute(pk, (shivam,))
            satish.commit()


        case 4:#update
        
            eid1 = int(input("Enter eid: "))
            ename1 = input("Enter ename: ")
            esel1 = float(input("Enter esel: "))
            pratik.execute("UPDATE student SET ename = %s, esel = %s WHERE eid = %s", (ename1, esel1, eid1))
            satish.commit()
        case 5:#drop database
            pratik.execute("drop database atm1001")
            satish.commit()

vimal = int(input("Enter (0:create database,1: Create Table, 2: Insert, 3: Delete, 4: Update):,5: drop databases "))
vish(vimal)
print("Success")




    
