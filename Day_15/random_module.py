import random

# Random integer
print("Random integer between 1 and 10:", random.randint(1, 10))

# Random choice from list
colors = ["red", "green", "blue"]
print("Random color:", random.choice(colors))

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)