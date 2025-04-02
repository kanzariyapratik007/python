class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"'{self.name}' by {self.salary}"
class dev:
    def __init__(self):
        self.emp=[]
    def add_emp(self,employee):
        self.emp.append(employee)
        print(f"employee'{employee.name}' name")
    def add_dev(self,developer):
        self.emp.append(developer)
        print(f"employee'{developer.name}' name")
    def add_int(self,intern):
        self.emp.append(intern)
        print(f"employee'{intern.name}' name")
def main():
    oop=emp()
    while True:
        print("\nemp manjment system")
        print("1. Add emp name")
        print("2. Add dev name")
        print("3. Add int name")
        choice = input("Enter your choice: ")

        if choice == "1":
           name = input("Enter Name: ")
           size = int(input("Enter size: "))
           salary = float(input("Enter Salary: "))
           oop.add_emp(name, size, salary)

        elif choice == "1":
           name = input("Enter Name: ")
           size = int(input("Enter size: "))
           salary = float(input("Enter Salary: "))
           oop.add_dev(name, size, salary)   
        
        elif choice == "1":
           name = input("Enter Name: ")
           size = int(input("Enter size: "))
           salary = float(input("Enter Salary: "))
           oop.add_int(name, size, salary)  

        else:
            print("Invalid choice, please try again.")  

if __name__ == "__main__":
   main()             
