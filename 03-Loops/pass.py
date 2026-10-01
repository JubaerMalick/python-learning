print("=== 1. PASS IN A FOR LOOP ===")
# Using pass as a placeholder for future implementation
for number in range(1, 6):
    if number == 3:
        # TODO: Add special logic for 3 later
        pass  # Python ignores this and continues normal execution
        print(f"Pass executed at number: {number}")
    else:
        print(f"Regular Number: {number}")


print("\n=== 2. DIFFERENCE BETWEEN PASS AND CONTINUE ===")
print("--- Using PASS ---")
for x in [1, 2, 3]:
    if x == 2:
        pass  # Does NOTHING, the next print() still executes!
    print(f"Pass loop item: {x}")

print("\n--- Using CONTINUE ---")
for x in [1, 2, 3]:
    if x == 2:
        continue  # SKIPS the next print() and goes to next iteration!
    print(f"Continue loop item: {x}")


print("\n=== 3. PASS IN CONDITIONAL BLOCKS & FUNCTIONS ===")
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    # Placeholder for special 18th birthday offer logic
    pass
else:
    print("Adult")


# Function placeholder using pass
def process_future_data():
    pass  # Will be implemented in the next sprint


print("\nProgram finished without any IndentationError!")