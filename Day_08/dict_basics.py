# Student details dictionary
student = {
    "name": "Jiyansh",
    "age": 18,
    "branch": "CSE - Data Science"
}

# Print original dictionary
print("Original Student Details:")
print(student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student["age"])

# Adding a new key
student["cgpa"] = 8.5

# Updating age
student["age"] = 19

# Deleting a key
del student["branch"]

# Print updated dictionary
print("\nUpdated Student Details:")
print(student)
