# Python Milestone Assessment

A set of two small console programs written in Python. Each one solves a separate problem and lives in its own folder with its own README, which describes the problem, the approach, the sample input and output, and the Python concepts it uses.

| Folder | Program | Summary |
|--------|---------|---------|
| [question1/](question1/) | Student Result Calculator | Collects marks in Python, SQL and AI for each student, then works out the total, average, grade and PASS/FAIL result, and summarises the class. See [question1/README.md](question1/README.md). |
| [question2/](question2/) | Employee File Manager | Stores employee records in `employees.txt`, reads them back, and reports on salaries, the highest-paid employee and the count of employees per role. See [question2/README.md](question2/README.md). |

## Requirements

- Python 3.7 or later
- Standard library only, no third-party packages to install

Check your version with:

```bash
python --version
```

## How to Run

Clone or download the repository, then run each program from its own folder.

**Student Result Calculator**

```bash
cd question1
python main.py
```

**Employee File Manager**

The program opens `employees.txt` from the current directory, so run it from inside `question2`:

```bash
cd question2
python main.py
```

## Repository Layout

```
python-milestone-assessment/
├── README.md              This file
├── .gitignore
├── question1/
│   ├── main.py            Student Result Calculator
│   └── README.md
└── question2/
    ├── main.py            Employee File Manager
    ├── employees.txt      Employee data (one record per line: ID,Name,Role,Salary)
    └── README.md
```

## Notes

- Each program is a standalone script. Running one does not affect the other.
