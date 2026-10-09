# ==========================================
# PYTHON LISTS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. LIST CREATION AND INDEXING ===")
# List with mixed data types
mixed_list = ["Python", 2026, 3.14, True]
print(f"Original List: {mixed_list}")

# Indexing (Positive & Negative)
print(f"First element: {mixed_list[0]}")
print(f"Last element: {mixed_list[-1]}")


print("\n=== 2. LIST SLICING ===")
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Original Numbers: {numbers}")
print(f"Index 1 to 4: {numbers[1:5]}")
print(f"First 3 elements: {numbers[:3]}")
print(f"Every 2nd element (Step 2): {numbers[::2]}")
print(f"Reversed List: {numbers[::-1]}")


print("\n=== 3. MODIFYING LISTS (ADD / REMOVE) ===")
fruits = ["Apple", "Banana"]

# Adding elements
fruits.append("Mango")           # Adds at the end
fruits.insert(1, "Orange")       # Adds at index 1
fruits.extend(["Grape", "Kiwi"]) # Adds multiple items
print(f"Updated Fruits: {fruits}")

# Removing elements
fruits.remove("Banana")          # Removes by value
popped_item = fruits.pop(2)      # Removes by index and returns value
print(f"Popped Item: {popped_item}")
print(f"List after removals: {fruits}")


print("\n=== 4. LIST OPERATIONS & BUILT-IN FUNCTIONS ===")
data = [45, 12, 89, 33, 7]

print(f"Length of list: {len(data)}")
print(f"Max value: {max(data)} | Min value: {min(data)}")
print(f"Sum of elements: {sum(data)}")

# Sorting
data.sort()
print(f"Sorted (Ascending): {data}")
data.sort(reverse=True)
print(f"Sorted (Descending): {data}")


print("\n=== 5. LIST COMPREHENSION ===")
# Syntax: [expression for item in iterable if condition]
# Generating squares of even numbers from 1 to 10
evens_squared = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Evens Squared: {evens_squared}")