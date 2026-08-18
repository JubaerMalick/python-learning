# Python Operators

# -------------------------
# 1. Arithmetic Operators
# -------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# -------------------------
# 2. Comparison Operators
# -------------------------

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# -------------------------
# 3. Assignment Operators
# -------------------------

x = 10

x += 5
print("After +=:", x)

x -= 3
print("After -=:", x)

x *= 2
print("After *=:", x)


# -------------------------
# 4. Logical Operators
# -------------------------

age = 25
has_id = True

print("AND:", age >= 18 and has_id)
print("OR:", age < 18 or has_id)
print("NOT:", not has_id)


# -------------------------
# 5. Membership Operators
# -------------------------

languages = ["Python", "JavaScript", "Java"]

print("Python in languages:", "Python" in languages)
print("C++ not in languages:", "C++" not in languages)


# -------------------------
# 6. Identity Operators
# -------------------------

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("a is b:", list_a is list_b)
print("a is c:", list_a is list_c)
