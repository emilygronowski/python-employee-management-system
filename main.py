def main() -> None:
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
                break
            case _:
                print()
                print("ERROR: Please enter a valid menu option.")


if __name__ == "__main__":
    main()
