# ==========================================
# PYTHON FOR LOOP - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC RANGE ITERATION ===")
# Loop from 0 to 4
for i in range(5):
    print(f"Iteration number: {i}")

# range(start, stop, step)
print("\nOdd numbers between 1 and 10:")
for num in range(1, 10, 2):
    print(num, end=" ")
print() # New line


print("\n=== 2. ITERATING OVER SEQUENCES (LIST & STRING) ===")
fruits = ["Apple", "Banana", "Mango", "Cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

print("\nIterating over characters in a String:")
word = "JUBAER"
for char in word:
    print(char, end="-")
print()


print("\n=== 3. ENUMERATE (GETTING INDEX & VALUE) ===")
languages = ["Python", "JavaScript", "C++", "Java"]

for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")


print("\n=== 4. LOOP CONTROL: BREAK AND CONTINUE ===")
print("--- Example of CONTINUE (Skip number 3) ---")
for count in range(1, 6):
    if count == 3:
        continue  # Skips print when count is 3
    print(f"Count: {count}")

print("--- Example of BREAK (Stop at number 4) ---")
for count in range(1, 10):
    if count == 4:
        print("Break condition met! Stopping loop.")
        break
    print(f"Count: {count}")


print("\n=== 5. FOR-ELSE BLOCK (SEARCH PATTERN) ===")
numbers = [10, 25, 40, 55, 70]
target = 40

for n in numbers:
    if n == target:
        print(f"Found target {target} in list!")
        break
else:
    # Runs only if the loop finishes normally without breaking
    print(f"Target {target} not found in list.")