# ==========================================
# PYTHON IF STATEMENT - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC IF STATEMENT ===")
age = 20

# Check if age is 18 or above
if age >= 18:
    print("You are an adult.")
    print("You are eligible to vote!")  # Indented lines belong to 'if'

print("This line always executes (outside if block).")


print("\n=== 2. IF WITH LOGICAL OPERATORS (AND, OR, NOT) ===")
has_id = True
is_vip = False

# Using 'and' (Both conditions must be True)
if age >= 18 and has_id:
    print("Access granted: Adult with valid ID.")

# Using 'or' (At least one condition must be True)
if age >= 18 or is_vip:
    print("Entry allowed: Either adult or VIP.")

# Using 'not' (Reverses boolean state)
is_blocked = False
if not is_blocked:
    print("User is active and not blocked.")


print("\n=== 3. TRUTHY AND FALSY VALUES ===")
# Non-empty string / non-zero numbers are evaluated as True
username = "Admin"
item_count = 3

if username:
    print(f"Welcome, {username}!")

if item_count:
    print(f"You have {item_count} items in your cart.")

# Empty values evaluate to False (This block won't print)
empty_cart = 0
if empty_cart:
    print("This will NOT print because 0 is Falsy.")


print("\n=== 4. NESTED IF (IF INSIDE IF) ===")
has_ticket = True
age = 10

if has_ticket:
    print("Ticket verified!")
    # Nested check inside the outer 'if'
    if age < 12:
        print("Ticket Price: Child ($5)")
    if age >= 12:
        print("Ticket Price: Standard ($10)")


print("\n=== 5. SHORT-HAND IF (ONE LINE) ===")
score = 85
if score > 80: print("Great score! You passed the high boundary.")