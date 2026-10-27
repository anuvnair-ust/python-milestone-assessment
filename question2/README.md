# Employee File Manager

A console program that stores employee records in a text file, reads them back, and prints a short report: all employees, those earning above ₹50,000, the highest-paid employee, and the number of employees in each role.

## Problem Statement

Build a simple Python application that maintains employee information. The program should:

1. Create and use a file called `employees.txt` to store employee details (Employee ID, Name, Role, Salary).
2. Read the employee information from the file.
3. Display all employees.
4. Find and display employees whose salary is greater than ₹50,000.
5. Find and display the employee with the highest salary.
6. Count how many employees belong to each role.
7. Use functions such as `add_employee()`, `read_employees()`, `find_highest_salary()` and `find_employees_by_role()`.
8. Use a context manager (`with open()`) when working with the file.
9. Handle the case where the file does not exist, using exception handling.
10. Use an `Employee` class with `employee_id`, `name`, `role` and `salary`, and a `display_details()` method.

## Approach and Logic

1. **Storage:** each employee is one line in `employees.txt`, in the form `ID,Name,Role,Salary`. `Employee.to_line()` builds that line and `add_employee()` appends it to the file.
2. **Reading:** `read_employees()` opens the file with `with open(...)`, skips blank lines, splits each line on commas with a list comprehension and creates an `Employee` object for each one. The salary is converted to an integer.
3. **Missing file:** if the file does not exist, `read_employees()` catches `FileNotFoundError`, prints a message and returns an empty list. The program then skips the report.
4. **Queries:**
   - `get_employees_above_cut_off_salary(employees)` keeps employees whose salary is strictly greater than `cut_off_salary`.
   - `find_highest_salary()` returns the employee with the largest salary, or `None` if the list is empty.
   - `find_employees_by_role(employees, role)` returns the employees with a given role.
   - `count_employees_by_role()` builds a dictionary of role to count, using `find_employees_by_role()` for each role.
5. **Output:** `display_results()` prints the whole report: all employees, the employees above the cut-off, the highest-paid employee and the count per role. Roles are printed in alphabetical order.

## Requirements

- Python 3.7 or later (standard library only, no third-party packages)

## How to Run

Run the program from the `question2` folder, because it opens `employees.txt` from the current directory:

```bash
cd question2
python main.py
```

## Sample Input

The input is the `employees.txt` file, which holds one employee per line:

```
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
105,Meera,Data Analyst,72000
106,Arjun,Developer,50001
107,Kavya,Project Manager,95000
108,Suresh,Tester,30000
109,Divya,QA Lead,51000
110,Vikram,Data Analyst,49999
111,Rohan,UI Designer,55000
112,Sneha Rao,Business Analyst,58000
```

When the program runs, it first asks whether you want to input employee details. Answer `n` to skip straight to the report. Answer `y` and it asks how many employees to add, then prompts for each employee's ID, name, role and salary. Each one is appended to `employees.txt` before the report is printed.

## Sample Output

```
Do you want to input employee details? (y/n): n

===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000
105 - Meera - Data Analyst - ₹72000
106 - Arjun - Developer - ₹50001
107 - Kavya - Project Manager - ₹95000
108 - Suresh - Tester - ₹30000
109 - Divya - QA Lead - ₹51000
110 - Vikram - Data Analyst - ₹49999
111 - Rohan - UI Designer - ₹55000
112 - Sneha Rao - Business Analyst - ₹58000

===== Employees with Salary > 50000 =====

John - ₹60000
Meera - ₹72000
Arjun - ₹50001
Kavya - ₹95000
Divya - ₹51000
Rohan - ₹55000
Sneha Rao - ₹58000

Highest Paid Employee:
Kavya - ₹95000

Employee Count by Role:
Business Analyst: 1
Data Analyst: 2
Developer: 2
Project Manager: 1
Python Developer: 1
QA Lead: 1
Tester: 3
UI Designer: 1
```

If `employees.txt` is missing, the program prints this and exits:

```
Error: 'employees.txt' not found. Add an employee to create it.
```

## Code Structure

| Item | Purpose |
|------|---------|
| `employee_file` | Name of the data file (`employees.txt`) |
| `cut_off_salary` | Salary threshold for the high-salary list (`50000`) |
| `Employee` class | Holds one employee; `display_details()` prints it, `to_line()` converts it to a file line |
| `add_employee(employee)` | Appends an employee to the file |
| `read_text(prompt)` | Asks for a text value, re-prompting if it is empty or contains a comma |
| `read_whole_number(prompt)` | Asks for a whole number, re-prompting if it is not one |
| `add_employees_from_user()` | Asks whether to add employees, how many, then prompts for each one and calls `add_employee()` |
| `read_employees()` | Reads the file and returns a list of `Employee` objects |
| `find_highest_salary(employees)` | Returns the highest-paid employee, or `None` |
| `find_employees_by_role(employees, role)` | Returns the employees with the given role |
| `get_employees_above_cut_off_salary(employees)` | Returns the employees earning more than `cut_off_salary` |
| `count_employees_by_role(employees)` | Returns a dictionary of role to number of employees |
| `display_results(employees)` | Prints the full report |

## Notes

- `add_employee()` is called by `add_employees_from_user()` only when the user answers `y` to the first prompt, so records are not appended on every run. Names, roles and IDs must not contain commas, and the program re-prompts if they do.
- The program sets the console output to UTF-8 with `sys.stdout.reconfigure()`, so the rupee sign (`₹`) prints even when the output is piped or redirected. Without it, a redirected run on Windows raises an encoding error.
- The file is parsed by splitting on commas, so names and roles must not contain commas.
- The program runs at module level: `add_employees_from_user()`, `read_employees()` and `display_results()` are called directly when the file is executed, with no `if __name__ == "__main__":` guard. Importing the file from another script will start the prompts and the report.

## Python Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Classes and objects | `Employee` class with `__init__`, `display_details()` and `to_line()` |
| Lists | The list of employees returned by `read_employees()` and passed to the query functions |
| Dictionaries | `count_employees_by_role()` builds role counts; the result is printed in `display_results()` |
| Functions | Every step of the program, such as `read_employees()`, `find_highest_salary()` and `display_results()` |
| Lambda function | `max(employees, key=lambda employee: employee.salary)` |
| File handling | `with open(...)` in `add_employee()` and `read_employees()`, with `"a"` for append and `"r"` for read |
| Exception handling | `try`/`except FileNotFoundError` in `read_employees()` |
| List comprehensions | Reading lines, creating `Employee` objects, filtering by role and by salary |
| Dictionary comprehension | `{role: len(find_employees_by_role(employees, role)) for role in roles}` in `count_employees_by_role()` |
| Generator expression | `set(employee.role for employee in employees)` in `count_employees_by_role()` |
| Conditional statements | `if` checks for empty lists and `None` results |
| Loops | `for` loops in reading and in `display_results()` |
| String methods | `strip()` to remove whitespace and newlines, `split(",")` to parse each line |
| Type conversion | `int(salary)` when reading the file |
| String formatting | f-strings in `display_details()` and `display_results()` |
| Module-level constants | `employee_file` and `cut_off_salary` |
| `sys.stdout.reconfigure()` | Sets UTF-8 output so the rupee sign prints, including when output is redirected |
