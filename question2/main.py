employee_file = "employees.txt"
cut_off_salary = 50000


class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")

    def to_line(self):
        return f"{self.employee_id},{self.name},{self.role},{self.salary}"


def add_employee(employee):
    with open(employee_file, "a", encoding="utf-8") as file:
        file.write(employee.to_line() + "\n")


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value and "," not in value:
            return value
        print("Please enter a value without commas.")


def read_whole_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def add_employees_from_user():
    while True:
        answer = input("Do you want to input employee details? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            break
        print("Please enter y or n.")

    if answer == "n":
        return

    count = read_whole_number("How many employees do you want to add? ")
    for number in range(1, count + 1):
        print(f"\nEmployee {number} of {count}")
        employee_id = read_text("Employee ID: ")
        name = read_text("Name: ")
        role = read_text("Role: ")
        salary = read_whole_number("Salary: ")
        add_employee(Employee(employee_id, name, role, salary))
    print()


def read_employees():
    try:
        with open(employee_file, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{employee_file}' not found. Add an employee to create it.")
        return []

    records = [line.split(",") for line in lines]
    return [Employee(employee_id, name, role, int(salary)) for employee_id, name, role, salary in records]


def find_highest_salary(employees):
    if not employees:
        return None
    return max(employees, key=lambda employee: employee.salary)


def find_employees_by_role(employees, role):
    return [employee for employee in employees if employee.role == role]


def get_employees_above_cut_off_salary(employees):
    return [employee for employee in employees if employee.salary > cut_off_salary]


def count_employees_by_role(employees):
    roles = sorted(set(employee.role for employee in employees))
    return {role: len(find_employees_by_role(employees, role)) for role in roles}


def display_results(employees):
    print("\n===== Employee Details =====\n")
    for employee in employees:
        employee.display_details()

    print(f"\n===== Employees with Salary > {cut_off_salary} =====\n")
    for employee in get_employees_above_cut_off_salary(employees):
        print(f"{employee.name} - ₹{employee.salary}")

    highest = find_highest_salary(employees)
    print("\nHighest Paid Employee:")
    print(f"{highest.name} - ₹{highest.salary}")

    print("\nEmployee Count by Role:")
    for role, count in count_employees_by_role(employees).items():
        print(f"{role}: {count}")

add_employees_from_user()

employees = read_employees()
if employees:
    display_results(employees)
