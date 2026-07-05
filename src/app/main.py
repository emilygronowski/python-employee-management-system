import csv

from app.models.employee import Employee


def load_employees() -> dict[int, Employee]:
    employees: dict[int, Employee] = {}

    try:
        with open("employees.csv", newline="") as data:
            reader = csv.reader(data)

            for row in reader:
                id = row[0]
                name = row[1]
                department = row[2]
                job_title = row[3]

                employees[int(id)] = Employee(name, department, job_title)

    except FileNotFoundError:
        pass

    return employees


def save_employees(employees: dict[int, Employee]) -> None:
    with open("employees.csv", "w") as file:
        for id, employee in employees.items():
            file.write(
                f"{id},{employee.name},{employee.department},{employee.job_title}\n"
            )


def main() -> None:
    employees = load_employees()
    print("Employee Management System")

    while True:
        print("\n1. Look up an employee")
        print("2. Add new employee")
        print("3. Edit employee")
        print("4. Delete employee")
        print("5. Exit")
        print()

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                save_employees(employees)
                break
            case _:
                print()
                print("ERROR: Please enter a valid menu option.")


if __name__ == "__main__":
    main()
