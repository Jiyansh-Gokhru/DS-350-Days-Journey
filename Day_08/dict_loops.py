# Dictionary of students and their marks
student_marks = {
    "Maths": 85,
    "Physics": 78,
    "Chemistry": 82,
    "English": 90
}

# Print all subjects and marks
print("Subject-wise Marks:")
for subject, marks in student_marks.items():
    print(subject, ":", marks)

# Calculate total marks
total = 0
for marks in student_marks.values():
    total += marks

print("\nTotal Marks:", total)
