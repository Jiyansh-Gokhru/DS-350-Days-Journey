# Student Data Logger

while True:
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    file = open("students.txt", "a")
    file.write(f"Name: {name}, Marks: {marks}\n")
    file.close()

    choice = input("Do you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        break

print("Student data saved successfully.")
