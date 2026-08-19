# ==========================================
# PYTHON TYPE CASTING COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. IMPLICIT TYPE CONVERSION (AUTOMATIC) ===")
num_int = 10       # Integer
num_float = 5.5    # Float

# Python automatically converts int to float to prevent data loss
result = num_int + num_float
print("Result:", result)
print("Result Type:", type(result))  # Output: <class 'float'>

print("\n=== 2. EXPLICIT TYPE CONVERSION (BASIC TYPES) ===")

# --- String/Float to Integer ---
price_str = "150"
price_int = int(price_str) # String -> Int
print("String to Int:", price_int, "| Type:", type(price_int))

pi_float = 3.99
pi_int = int(pi_float)     # Float -> Int (Truncates decimals, data loss!)
print("Float to Int (Data Loss):", pi_int) # Output: 3

# --- Int/String to Float ---
age = 25
age_float = float(age)     # Int -> Float
print("Int to Float:", age_float) # Output: 25.0

# --- Anything to String ---
score = 98.5
score_str = str(score)     # Float -> String
greeting = "Your score is " + score_str  # String concatenation
print(greeting)

# --- Boolean Conversion (Truthy & Falsy Values) ---
print("bool(1):", bool(1))        # True
print("bool(0):", bool(0))        # False
print("bool('Hello'):", bool("Hello")) # True (Non-empty string)
print("bool(''):", bool(""))      # False (Empty string)


print("\n=== 3. DATA STRUCTURE CONVERSIONS ===")

# --- List to Tuple and Set ---
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", my_list)

my_tuple = tuple(my_list) # List -> Tuple
print("List to Tuple:", my_tuple)

my_set = set(my_list)     # List -> Set (Removes duplicates automatically)
print("List to Set (Unique items):", my_set)

# --- Tuple of Key-Value pairs to Dictionary ---
pair_list = [("name", "Rahim"), ("age", 22), ("city", "Dhaka")]
my_dict = dict(pair_list) # Tuple List -> Dictionary
print("Pairs to Dict:", my_dict)


print("\n=== 4. ERROR HANDLING IN TYPE CASTING ===")
# Invalid conversion test
invalid_str = "abc123"

try:
    converted_num = int(invalid_str) # Will throw ValueError
except ValueError:
    print(f"Error: '{invalid_str}' ke Integer-e convert kora jabe na!")