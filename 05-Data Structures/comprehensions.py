# ==========================================
# PYTHON COMPREHENSIONS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. LIST COMPREHENSION ===")
# Traditional way vs List Comprehension
# Goal: Get squares of even numbers from 1 to 10

# Traditional Method:
traditional_squares = []
for x in range(1, 11):
    if x % 2 == 0:
        traditional_squares.append(x ** 2)

# List Comprehension Method:
# Syntax: [expression for item in iterable if condition]
comprehension_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

print(f"Traditional Result: {traditional_squares}")
print(f"Comprehension Result: {comprehension_squares}")


print("\n=== 2. LIST COMPREHENSION WITH IF-ELSE ===")
# Syntax: [true_expr if condition else false_expr for item in iterable]
# Label numbers as "Even" or "Odd"
numbers = [1, 2, 3, 4, 5, 6]
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(f"Original: {numbers}")
print(f"Labels: {labels}")


print("\n=== 3. DICTIONARY COMPREHENSION ===")
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Creating a dictionary of word lengths
words = ["python", "code", "comprehension", "list"]
word_lengths = {word: len(word) for word in words}
print(f"Word Lengths: {word_lengths}")

# Filtering Dictionary: Only keep items with price > 100
prices = {"apple": 50, "mango": 120, "banana": 30, "dragonfruit": 250}
expensive_fruits = {item: price for item, price in prices.items() if price > 100}
print(f"Expensive Fruits (>100): {expensive_fruits}")


print("\n=== 4. SET COMPREHENSION ===")
# Syntax: {expression for item in iterable if condition}
# Automatically removes duplicates and applies expression

names = ["rahim", "karim", "rahim", "jubaer", "JUBAER"]
# Extract unique lengths of names
unique_name_lengths = {len(name) for name in names}
print(f"Unique Name Lengths Set: {unique_name_lengths}")


print("\n=== 5. NESTED LIST COMPREHENSION ===")
# Flattening a 2D Matrix (List of Lists) into a 1D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]
print(f"Original 2D Matrix: {matrix}")
print(f"Flattened 1D List: {flattened}")