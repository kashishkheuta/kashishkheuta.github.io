# Student Result Management System

students = {}

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    marks = []
    for i in range(1, 6):
        m = int(input(f"Enter marks of subject {i}: "))
        marks.append(m)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    students[roll] = {
        "Name": name,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    print("✅ Student added successfully\n")

def display_students():
    print("\n--- Student Results ---")
    for roll, data in students.items():
        print(f"""
Roll No     : {roll}
Name        : {data['Name']}
Total Marks : {data['Total']}
Percentage  : {data['Percentage']}%
Grade       : {data['Grade']}
-------------------------
""")

while True:
    print("1. Add Student")
    print("2. Display Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("❌ Invalid choice")
