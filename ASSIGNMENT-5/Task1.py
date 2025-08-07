students_data = {}
student_name = input("Enter the student's name: ")
student_marks = input(f"{student_name}'s marks: ")

students_data[student_name] = student_marks
search_record = input("Enter the student's name: ")
if search_record in students_data: 
    print(f"{search_record}'s marks: {students_data[search_record]}")
else: 
    print("Student not found.")