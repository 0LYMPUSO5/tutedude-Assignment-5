# Task 1: Create a Dictionary of Student Marks
'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student's name is not found, display an appropriate message.'''

# Create a dictionary with student names as keys and marks as values
students_record = {
    "Anish Negi" : 90,
    "Alice" : 85,
    "Anjali Negi" : 95,
    "Anisha" : 80
}
# input a student's name
name = input("Enterr the students's name: ")

if name in students_record:
    print(f"{name}'s marks: {students_record[name]}")
else:
    print("Student not found.")