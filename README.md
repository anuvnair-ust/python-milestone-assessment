# Python Milestone Assessment

Two small console programs, each solving a scenario-based task with basic Python concepts. Each question has its own folder and its own README with more detail.

| Folder | Program | Summary |
|--------|---------|---------|
| [question1/](question1/) | Student Marks Management System | Collects marks in Python, SQL and AI for each student, then works out the total, average, grade and PASS/FAIL result, and summarises the class. |
| [question2/](question2/) | Simple Employee File Management | Stores employee records in `employees.txt`, reads them back, and reports on salaries, the highest-paid employee and the count of employees per role. |

## Requirements

- Python 3.7 or later
- Standard library only, no third-party packages to install

Check your version with:

```bash
python --version
```

## Repository Layout

```
python-milestone-assessment/
├── question1/
│   ├── main.py            Student marks program
│   └── README.md
├── question2/
│   ├── main.py            Employee file program
│   ├── employees.txt      Employee data (one record per line: ID,Name,Role,Salary)
│   └── README.md
└── README.md
```

---

## Question 1 — Student Marks Management System

### Problem Statement

Build a simple Python program that accepts details of multiple students, calculates their results, and displays a summary. The program should:

1. Store each student's Student ID, Name, Python marks, SQL marks and AI marks.
2. Calculate the Total, Average and Grade for each student.
3. Show whether each student is PASS (average 40 or more) or FAIL (average below 40).
4. Show the student with the highest average.
5. Show the students whose average is more than 75.
6. Present the final result in a readable format.

### Approach and Logic

1. **Input:** `get_no_of_students()` asks for the number of students. `get_student_data()` runs once per student and builds a dictionary with the ID, name and a `marks` dictionary that maps each subject to its mark.
2. **Calculation:** `calculate_result()` adds the marks to get the total, divides by the number of subjects to get the average, and sets the grade and result on the same dictionary.
3. **Grade and result:** `calculate_grade()` maps the average to a grade. `get_result()` returns `PASS` for an average of 40 or more, otherwise `FAIL`.

   | Average        | Grade |
   |----------------|-------|
   | 75 and above   | A     |
   | 60 to below 75 | B     |
   | 50 to below 60 | C     |
   | 40 to below 50 | D     |
   | Below 40       | E     |

4. **Summary:** `get_highest_scorer()` returns every student with the highest average. `get_students_above_cut_off_marks()` returns the names of students whose average is above 75.
5. **Output:** `display_results()` prints each student's report, then the highest scorer and the above-75 list.

### How to Run

```bash
cd question1
python main.py
```

### Sample Input

Typed at the prompts (two students):

```
2
101
Rahul
80
95
90
102
Anjali
60
70
65
```

### Sample Output

```
Enter total number of students: 2

Enter Student ID: 101
Enter Student Name: Rahul
Enter Python marks for Rahul: 80
Enter SQL marks for Rahul: 95
Enter AI marks for Rahul: 90

Enter Student ID: 102
Enter Student Name: Anjali
Enter Python marks for Anjali: 60
Enter SQL marks for Anjali: 70
Enter AI marks for Anjali: 65

===== Student Result =====

Student ID: 101
Name: Rahul
Total: 265.0
Average: 88.33
Grade: A
Result: PASS

Student ID: 102
Name: Anjali
Total: 195.0
Average: 65.00
Grade: B
Result: PASS

Highest Scoring Student: Rahul
Students above 75: Rahul
```

### Python Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Lists | `subjects`, the list of student records, the list of names returned by the summary functions |
| Dictionaries | Each student record (`id`, `name`, `marks`), and the `marks` dictionary keyed by subject |
| Functions | `get_marks()`, `calculate_result()`, `get_highest_scorer()`, `display_results()` and the others |
| Conditional statements | `if`/`elif`/`else` in `calculate_grade()`, `if` checks in `get_marks()` and `get_result()` |
| Loops | `while True` for re-prompting invalid input, `for` loops in comprehensions and `display_results()` |
| List comprehensions | `get_student_data()`, `get_student_details()`, `get_students_above_cut_off_marks()`, `get_highest_scorer()` |
| Dictionary comprehension | `marks = {subject: get_marks(...) for subject in subjects}` in `get_student_data()` |
| Generator expression | `max(student["average_marks"] for student in students)` |
| Exception handling | `try`/`except ValueError` for non-numeric input |
| String formatting | f-strings, and the `:.2f` format spec for averages |

---

## Question 2 — Simple Employee File Management

### Problem Statement

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

### Approach and Logic

1. **Storage:** each employee is one line in `employees.txt`, in the form `ID,Name,Role,Salary`. `Employee.to_line()` builds the line and `add_employee()` appends it to the file.
2. **Reading:** `read_employees()` opens the file with `with open(...)`, skips blank lines, splits each line on commas and creates an `Employee` object for each one. The salary is converted to an integer.
3. **Missing file:** if the file does not exist, `read_employees()` catches `FileNotFoundError`, prints a message and returns an empty list. The report is then skipped.
4. **Queries:**
   - `get_employees_above_cut_off_salary(employees)` keeps employees whose salary is strictly greater than 50,000.
   - `find_highest_salary(employees)` returns the employee with the largest salary, or `None` if the list is empty.
   - `find_employees_by_role(employees, role)` returns the employees with a given role.
   - `count_employees_by_role(employees)` builds a dictionary of role to count.
5. **Output:** `display_results()` prints all employees, the employees above the cut-off, the highest-paid employee and the count per role. Roles are printed in alphabetical order.

### How to Run

The program opens `employees.txt` from the current directory, so run it from inside `question2`:

```bash
cd question2
python main.py
```

Answer `n` to the first prompt to skip adding employees and go straight to the report. Answer `y` to add employees; each one is appended to `employees.txt` before the report is printed.

### Sample Input

The `employees.txt` file, one employee per line:

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

Typed at the first prompt, to skip adding employees:

```
n
```

### Sample Output

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

If `employees.txt` is missing, the program prints this and skips the report:

```
Error: 'employees.txt' not found. Add an employee to create it.
```

### Python Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Classes and objects | `Employee` class with `__init__`, `display_details()` and `to_line()` |
| Lists | The list of employees returned by `read_employees()` and passed to the query functions |
| Dictionaries | `count_employees_by_role()` builds role counts; the result is printed in `display_results()` |
| Functions | `add_employee()`, `read_employees()`, `find_highest_salary()`, `find_employees_by_role()` and the others |
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

---

## Notes

- Each program is a standalone script. Running one does not affect the other.
- The question-level READMEs in [question1/](question1/README.md) and [question2/](question2/README.md) include the full code structure tables and extra notes.
