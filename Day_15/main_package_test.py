# Importing from package
from text_processing.string_ops import reverse_string
from text_processing.file_ops import read_file

# Test reverse_string
text = "Python"
print("Original:", text)
print("Reversed:", reverse_string(text))

# Test read_file
# Create a sample file first
with open("sample.txt", "w") as f:
    f.write("Hello World!\nWelcome to Python Packages.\nEnjoy coding!")

# Now read it using our package function
read_file("sample.txt")