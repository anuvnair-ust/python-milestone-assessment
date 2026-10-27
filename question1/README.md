# Student Result Calculator

A console program that collects marks for a group of students in three subjects (Python, SQL, AI), then calculates each student's total, average, grade and pass/fail result. It finishes by printing a summary of all students.

## Problem Statement

Build a simple Python program to manage student marks. The program should:

1. Store each student's Student ID, Name, Python marks, SQL marks and AI marks.
2. Calculate the Total, Average and Grade for each student.
3. Show whether each student is PASS (average 40 or more) or FAIL (average below 40).
4. Show the student with the highest average.
5. Show the students whose average is more than 75.
6. Present the final result in a readable format.

## Approach and Logic

1. **Input:** `get_no_of_students()` asks for the number of students. `get_student_data()` then runs once per student and builds a dictionary holding the ID, name and a `marks` dictionary that maps each subject to its mark.
2. **Calculation:** `calculate_result()` adds the marks to get the total, divides by the number of subjects to get the average, and then sets the grade and result. The fields are added to the same student dictionary and that dictionary is returned.
3. **Grade and result:** `calculate_grade()` checks the average against the grading scale below, and `get_result()` returns `PASS` or `FAIL`.
4. **Summary:** `get_highest_scorer()` finds the maximum average and returns every student who has it. `get_students_above_cut_off_marks()` keeps the names of students whose average is above `cut_off_mark`.
5. **Output:** `display_results()` prints each student's report, then the highest scorer and the above-cut-off list.

## Requirements

- Python 3.x (standard library only, no third-party packages)

## How to Run

```bash
python main.py
```

## Usage

The program prompts for input in this order:

1. **Total number of students.** Must be a whole number greater than 0.
2. For each student:
   - **Student ID** (free text)
   - **Student Name** (free text)
   - **Marks** for Python, SQL and AI. Each must be a number from 0 to 100.

Invalid input is rejected and the same prompt is shown again until a valid value is entered.

## Sample Input

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

## Sample Output

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

### Single-student example

```
Enter total number of students: 1

Enter Student ID: S001
Enter Student Name: Asha
Enter Python marks for Asha: 80
Enter SQL marks for Asha: 65
Enter AI marks for Asha: 90

===== Student Result =====

Student ID: S001
Name: Asha
Total: 235.0
Average: 78.33
Grade: A
Result: PASS

Highest Scoring Student: Asha
Students above 75: Asha
```

## Output

For each student, the program displays:

| Field   | Description                                              |
|---------|----------------------------------------------------------|
| Total   | Sum of the three subject marks                           |
| Average | Total divided by the number of subjects                  |
| Grade   | Letter grade based on the average (see below)            |
| Result  | `PASS` if the average is 40 or more, otherwise `FAIL`    |

After the individual results, the program shows:

- **Highest Scoring Student:** every student whose average equals the highest average. More than one name is listed if there is a tie.
- **Students above 75:** students whose average is strictly greater than 75. Shows `None` if nobody qualifies.

### Grading Scale

| Average        | Grade |
|----------------|-------|
| 75 and above   | A     |
| 60 to below 75 | B     |
| 50 to below 60 | C     |
| 40 to below 50 | D     |
| Below 40       | E     |

## Configuration

Two values near the top of `main.py` control the program:

- `subjects`: the list of subject names. Each student is asked for marks in every subject listed here.
- `cut_off_mark`: the average used for the "Students above" summary (default `75`).

## Code Structure

| Function                             | Purpose                                                        |
|--------------------------------------|----------------------------------------------------------------|
| `get_marks(subject, student_name)`   | Prompts for one mark until a value from 0 to 100 is entered    |
| `get_no_of_students()`               | Prompts for the number of students until a value above 0 is entered |
| `get_student_data()`                 | Collects the ID, name and marks of one student                 |
| `calculate_grade(average)`           | Maps an average to a letter grade                              |
| `get_result(average)`                | Returns `PASS` or `FAIL`                                       |
| `calculate_result(students)`         | Adds total, average, grade and result to a student record      |
| `get_student_details()`              | Collects and calculates results for all students               |
| `get_students_above_cut_off_marks()` | Returns the names of students above `cut_off_mark`             |
| `get_highest_scorer()`               | Returns the name(s) of the student(s) with the highest average |
| `display_results()`                  | Prints the full report                                         |

The program runs at module level: `get_student_details()` and `display_results()` are called directly when the file is executed, with no `if __name__ == "__main__":` guard. Importing the file from another script will start the prompts.

## Notes

- Marks can be decimals (for example `78.5`). Marks are read as floats, so the total is shown as a float (for example `265.0`). The average is shown with two decimal places (`:.2f`).
- The student ID is not checked for uniqueness or for an empty value.
- The average is computed from the marks entered, so the divisor is the number of subjects in `subjects`.

## Python Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Variables and constants | `subjects`, `cut_off_mark` at module level |
| Lists | `subjects`, the list of student records, the list of names returned by the summary functions |
| Dictionaries | Each student record (`id`, `name`, `marks`), and the `marks` dictionary keyed by subject |
| Functions | Every step of the program, such as `get_marks()`, `calculate_result()`, `get_highest_scorer()` |
| Return values | Functions return values that `display_results()` prints |
| Conditional statements | `if`/`elif`/`else` in `calculate_grade()`, `if` checks in `get_marks()` and `get_result()` |
| Loops | `while True` for re-prompting invalid input, `for` loops in comprehensions and `display_results()` |
| List comprehensions | `get_student_data()` (list of students), `get_student_details()`, `get_students_above_cut_off_marks()`, `get_highest_scorer()` |
| Dictionary comprehension | `marks = {subject: get_marks(...) for subject in subjects}` in `get_student_data()` |
| Generator expression | `max(student["average_marks"] for student in students)` |
| Exception handling | `try`/`except ValueError` for non-numeric input |
| Built-in functions | `input()`, `float()`, `int()`, `sum()`, `len()`, `max()`, `print()`, `range()` |
| String formatting | f-strings, and the `:.2f` format spec for averages |
| Logical `or` | `", ".join(...) or "None"` to show a default when the list is empty |
