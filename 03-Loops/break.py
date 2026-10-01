
print("=== 1. BASIC BREAK IN A FOR LOOP ===")
# Stopping a loop when a target number is reached
for num in range(1, 10):
    if num == 5:
        print("Target 5 reached! Executing break...")
        break
    print(f"Current Number: {num}")

print("Loop finished and exited successfully.")


print("\n=== 2. SEARCHING IN A LIST USING BREAK ===")
# Efficient searching: Stop as soon as the item is found
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
search_item = "Keyboard"

for index, product in enumerate(products):
    print(f"Checking item {index + 1}: {product}")
    if product == search_item:
        print(f"FOUND! '{search_item}' is available in stock.")
        break  # No need to check 'Monitor' or 'Headphones'


print("\n=== 3. BREAK IN NESTED LOOPS ===")
# 'break' only stops the INNERMOST loop where it is placed
for outer in range(1, 4):
    print(f"\nOuter Loop Iteration: {outer}")
    for inner in range(1, 4):
        if inner == 2:
            print("   Inner loop encountered break at 2!")
            break  # Stops inner loop, but outer loop continues
        print(f"   Inner Loop Value: {inner}")


print("\n=== 4. BREAK WITH FOR-ELSE BLOCK ===")
numbers = [2, 4, 6, 8, 9, 10]

# Checking if list contains any odd number
for n in numbers:
    if n % 2 != 0:
        print(f"First odd number found: {n}")
        break
else:
    # This block executes ONLY if loop finishes WITHOUT hitting break
    print("All numbers are even (no break occurred).")