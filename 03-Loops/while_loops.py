
print("=== 1. BASIC WHILE LOOP ===")
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment (Must update variable to prevent infinite loop!)


print("\n=== 2. USING WHILE LOOP WITH BREAK & CONTINUE ===")
number = 0

print("--- Skip even numbers (Continue) & Stop at 7 (Break) ---")
while number < 10:
    number += 1
    
    if number % 2 == 0:
        continue  # Skips even numbers
        
    if number == 7:
        print("Reached 7! Breaking the loop.")
        break  # Stops the loop completely
        
    print(f"Odd Number: {number}")


print("\n=== 3. WHILE LOOP FOR USER INPUT & VALIDATION ===")
# Interactive input simulation loop
secret_number = 5
attempts = 0
max_attempts = 3

# Dummy guess list to simulate user input during automated execution
simulated_inputs = [2, 8, 5]

while attempts < max_attempts:
    guess = simulated_inputs[attempts]  # Simulating user input
    attempts += 1
    print(f"Attempt {attempts}: User guessed {guess}")
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break
else:
    # Runs only if the while loop completes naturally without hitting 'break'
    print("❌ Out of attempts! Better luck next time.")


print("\n=== 4. WHILE-ELSE STRUCTURE ===")
n = 3
while n > 0:
    print(f"Countdown: {n}")
    n -= 1
else:
    print("Blastoff! Countdown completed successfully without break.")