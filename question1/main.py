subjects = ["Python", "SQL", "AI"]
cut_off_mark = 75


def get_marks(subject,student_name):    
    while True:
        try:
            mark = float(input(f"Enter {subject} marks for {student_name}: "))

            if 0<= mark <=100:
                return mark
            print("Please enter a number between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

def get_no_of_students():
    while True:
        try:
            no_of_students = int(input("Enter total number of students: "))
            if no_of_students > 0:
                return no_of_students
            print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

def get_student_data(position,total):    
    print(f"\nStudent {position} of {total}")
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    marks = {subject : get_marks(subject, student_name) for subject in subjects}
    students = {"id": student_id, "name": student_name, "marks": marks}
    return students


def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >=50:
        return "C"
    elif average >= 40:
        return "D"
    return "E"

def get_result(average):
    if average >= 40 :
        return "PASS"
    return "FAIL"


def calculate_result(students):
    total = sum(students["marks"].values())
    average = total / len(students["marks"])
    students["total_marks"] = total
    students["average_marks"] = average
    students["grade"] = calculate_grade(average)
    students["result"] = get_result(average)
    return students

def get_student_details():
    no_of_students = get_no_of_students()
    student_data = [get_student_data(position,no_of_students) for position in range(1,no_of_students+1)]
    student_result = [calculate_result(student) for student in student_data]
    return student_result


def get_students_above_cut_off_marks(students):
    students_list = [student["name"] for student in students if student["average_marks"] > cut_off_mark]
    return students_list

def get_highest_scorer(students):
    max_score = max(student["average_marks"] for student in students)
    return [student["name"] for student in students if student["average_marks"] == max_score]


def display_results(students):
    print("\n===== Student Result =====\n")

    for student in students:
        print(f"Student ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Total: {student['total_marks']}")
        print(f"Average: {student['average_marks']:.2f}")
        print(f"Grade: {student['grade']}")
        print(f"Result: {student['result']}\n" )

    above_students = ", ".join(get_students_above_cut_off_marks(students)) or "None"

    print("Highest Scoring Student:", ", ".join(get_highest_scorer(students)))
    print(f"Students above {cut_off_mark}: {above_students}")


details = get_student_details()
display_results(details)