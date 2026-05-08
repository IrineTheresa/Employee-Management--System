employees = []

def add_employee():
    id=int(input("Enter the employee id:"))
    name=input("Enter employee name:")
    Email=input("Enter email:")
    Department=input("Enter department:")
    Salary=float(input("Enter salary:"))
    Status=input("Enter status:")
    employee={
    "id":id,
    "name":name,
    "Email":Email,
    "Department":Department,
    "Salary":Salary,
    "Status":"ACTIVE"
}
    employees.append(employee)
    print("employees added successfully")
   

def fetch_employee():
    id=int(input("Enter employee id:"))
    for emp in employees:
        if emp["id"]==id:
         print(emp)
         return
    print("Employee not found")

def fetch_all_employee():
    print("\nActive employees:")
    found = False
    for emp in employees:
        if emp["Status"] == "ACTIVE":
            print(emp)
            found = True
    if not found:
        print("\nNo active employees found")

def update_employee():
    id=int(input("Enter employee id:"))
    for emp in employees:
        if emp["id"]==id:
            emp["name"]=input("Enter new name:")
            emp["Email"]=input("Enter new email:")
            emp["Department"]=input("Eter new epartment:")
            emp["Salary"]=float(input("Enter new Salary:"))
            emp["Status"]=input("Enter new status:")
            print("employee updated successfully\n")
        print("employee not found")           
def delete_employee():
    id=int(input("Enter employee id:"))
    for emp in employees:
        if emp["id"]==id:
            emp["Status"]="INACTIVE"
            print("\n Employee marked as inactive successfully")
            return
        print("\n Employee not found")
while True:
            print("\n EMPLOYEE MANAGEMENT SYSYTEM")
            print("\n 1. Add Employee")
            print("\n 2.Fetch Employee By ID")
            print("\n 3. Fetch All Employees By Status")
            print("\n 4.Update Employee")
            print("\n 5.Delete Employee")
            print("\n 6.Exit")
            choice=input("Enter your choice:")
            if choice=="1":
             add_employee()
            elif choice=="2":
                fetch_employee()
            elif choice=="3":
                fetch_all_employee()
            elif choice=="4":
                update_employee()
            elif choice=="5":
                delete_employee()
            elif choice=="6":
                print("Exiting...")
                break
            else:
                print("Invalid choice")
                                