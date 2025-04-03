class emp:
    def __init__(self,name,salary,size):
        self.name=name
        self.salary=salary
        self.size=size
    def __str__(self):
        return f"'{self.name}' by {self.salary} by {self.size}"
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
    oop=dev()
    while True:
        print("\nemp manjment system")
        print("1. Add emp name")
        print("2. Add dev name")
        print("3. Add int name")
        choice = input("Enter your choice: ")

        if choice == "1":
           name = input("Enter emp Name: ")
           size = int(input("Enter emp size: "))
           salary = int(input("Enter emp Salary: "))
           employee = emp(name, salary, size)
           oop.add_emp(employee)

        elif choice == "2":
           name = input("Enter dev Name: ")
           size = int(input("Enter dev size: "))
           salary = int(input("Enter dev Salary: "))
           employee = emp(name, salary, size)
           oop.add_dev(employee) 
        
        elif choice == "3":
           name = input("Enter int Name: ")
           size = int(input("Enter int size: "))
           salary = int(input("Enter int Salary: "))
           employee = emp(name, salary, size)
           oop.add_int(employee)

        else:
            print("sorry")  

if __name__ == "__main__":
   main()             
