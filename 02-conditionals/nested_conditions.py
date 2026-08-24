# ==========================================
# PYTHON NESTED CONDITIONS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC NESTED IF (ATM SIMULATION) ===")
card_inserted = True
pin_correct = True
balance = 5000
withdraw_amount = 2000

# Outer Condition
if card_inserted:
    print("Card Accepted!")
    
    # Inner Condition 1
    if pin_correct:
        print("PIN Verified.")
        
        # Inner Condition 2 (Nested inside PIN check)
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal Successful! Remaining Balance: ${balance}")
        else:
            print("Error: Insufficient Balance!")
            
    else:
        print("Error: Invalid PIN!")
        
else:
    print("Error: Please insert a valid card.")


print("\n=== 2. NESTED IF VS 'AND' OPERATOR DIFFERENCE ===")
age = 22
has_license = True

# --- Approach A: Using Nested IF ---
print("--- Using Nested IF ---")
if age >= 18:
    print("Age Check: Passed.")
    if has_license:
        print("Driving Status: Allowed to drive legally!")
    else:
        print("Driving Status: Need to get a license first!")

# --- Approach B: Using Logical AND ---
print("--- Using Logical AND ---")
if age >= 18 and has_license:
    print("Driving Status: Allowed to drive legally!")
# (Note: Logical 'and' doesn't let you print individual messages for age pass/fail easily)


print("\n=== 3. COMPLEX LOAN ELIGIBILITY SYSTEM ===")
salary = 45000
credit_score = 720
employment_years = 3

if salary >= 30000:
    print("Step 1 Passed: Minimum Salary Requirement Met.")
    
    if credit_score >= 700:
        print("Step 2 Passed: Good Credit Score.")
        
        if employment_years >= 2:
            print("CONGRATS: Your loan application is APPROVED!")
        else:
            print("REJECTED: Need at least 2 years of work experience.")
            
    else:
        print("REJECTED: Credit score is too low.")
        
else:
    print("REJECTED: Salary below required threshold.")