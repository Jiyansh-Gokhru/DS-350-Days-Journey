text = input("Enter a string: ")

print("Total characters:", len(text))
print("Total words:", len(text.split()))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed:", text[::-1])

vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

print("Starts with vowel:", text[0] in vowels)
print("With underscores:", text.replace(" ", "_"))
