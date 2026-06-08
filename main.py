import employee_manager as em


def main():
    #menu loop 
    while True:
        print("\nEmployee Management System")
        print("1. Look up an employee")
        print("2. Add new employee")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        #Look up an employee
        if choice == "1":
            emp_id = int(input("Enter ID to look up: "))
            employee = em.get_employee(emp_id)
            print(employee if employee else "Employee not found")

        #add an employee
        elif choice == '2':
            emp_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            title = input("Enter Job Title: ")
            em.add_employee(emp_id, name, dept, title)
            print("Employee Created")

        #edit an employee
        elif choice == '3':
            emp_id = int(input("Enter Employee ID to edit: "))
            name = input("Enter new Name (or leave blank): ")
            dept = input("Enter new Dept (or leave blank): ")
            title = input("Enter new Title (or leave blank): ")
            success = em.edit_employee(emp_id, name or None, dept or None, title or None)
            print("Updated successfully." if success else "Error: ID not found.")

        #delete an employee
        elif choice == '4':
            emp_id = int(input("Enter Employee ID to delete: "))
            success = em.delete_employee(emp_id)
            print("Employee deleted!" if success else "Error: ID not found.")

        #exit
        elif choice == '5':
            print("Exiting program...")
            break #break menu loop

        else: #invalid input
            print("Erros: Please enter one of the values shown")

if __name__ == "__main__":
    main()
