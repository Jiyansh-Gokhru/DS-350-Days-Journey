numbers = {10, 20, 30, 40, 50}
print(numbers)

data = {1, 2, 2, 3, 3, 4}
print(data)   # duplicates removed

numbers.add(60)
print(numbers)

numbers.remove(20)   # error if element not found
print(numbers)

numbers.discard(100) # no error even if not found
print(numbers)

removed_item = numbers.pop()
print("Removed:", removed_item)
print(numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

