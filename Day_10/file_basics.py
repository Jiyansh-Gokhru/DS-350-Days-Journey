
# Writing data to a file
file = open("my_info.txt", "w")
file.write("Name: Jiyansh Jain\n")
file.write("Age: 18\n")
file.write("Branch: CSE Data Science\n")
file.close()

# Reading data from the file
file = open("my_info.txt", "r")
content = file.read()
print(content)
file.close()
