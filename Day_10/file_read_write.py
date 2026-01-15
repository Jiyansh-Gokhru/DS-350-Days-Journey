
# Writing multiple lines
file = open("practice.txt", "w")
file.write("Python\n")
file.write("Data Science\n")
file.write("Machine Learning\n")
file.write("Deep Learning\n")
file.write("AI\n")
file.close()

# Read entire file
file = open("practice.txt", "r")
print("Full content:")
print(file.read())
file.close()

# Read line by line
file = open("practice.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())
file.close()

# Append a new line
file = open("practice.txt", "a")
file.write("Generative AI\n")
file.close()
