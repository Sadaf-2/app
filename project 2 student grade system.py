python

students = {}

def add_student(name, marks):
    grade = "A" if marks >= 80 else "B" if marks >= 60 else "C"
    students[name] = {"marks": marks, "grade": grade}
    print("Student added.")

def view_students():
    for name, info in students.items():
        print(f"{name}: Marks={info['marks']}, Grade={info['grade']}")

while True:
    print("\n1. Add Student\n2. View All\n3. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Student name: ")
        try:
            marks = int(input("Marks: "))
            add_student(name, marks)
        except ValueError:
            print("Please enter valid marks.")
    elif ch == '2':
        view_students()
    elif ch == '3':
        break
    else:
        print("Invalid option.")
