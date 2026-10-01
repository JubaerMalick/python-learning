print("=== 1. BASIC CONTINUE IN A FOR LOOP ===")
# Skipping number 3 in a range
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3 using continue...")
        continue
    print(f"Number: {num}")


print("\n=== 2. FILTERING EVEN/ODD NUMBERS ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Printing only odd numbers:")
for n in numbers:
    if n % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd Number: {n}")


print("\n=== 3. PROCESSING VALID DATA (SKIPPING INVALID DATA) ===")
# Skipping invalid scores (negative or above 100)
scores = [85, -10, 92, 105, 78, 0, 95]

print("Valid exam scores:")
for score in scores:
    if score < 0 or score > 100:
        print(f"Skipping invalid score: {score}")
        continue
    print(f"Valid Score: {score}")


print("\n=== 4. CONTINUE IN WHILE LOOP ===")
# Be careful: Update the counter BEFORE 'continue' to avoid infinite loops!
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count 3 in while loop...")
        continue
    print(f"While Loop Count: {count}")