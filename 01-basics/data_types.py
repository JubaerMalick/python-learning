# ==========================================
# Python Data Types
# ==========================================


# ------------------------------------------
# 1. String (str)
# ------------------------------------------

name = "Hedaetullah"
university = "Daffodil International University"

print("Name:", name)
print("University:", university)
print("Name Data Type:", type(name))


# ------------------------------------------
# 2. Integer (int)
# ------------------------------------------

age = 25
graduation_year = 2025

print("\nAge:", age)
print("Graduation Year:", graduation_year)
print("Age Data Type:", type(age))


# ------------------------------------------
# 3. Float (float)
# ------------------------------------------

cgpa = 3.81
height = 5.8

print("\nCGPA:", cgpa)
print("Height:", height)
print("CGPA Data Type:", type(cgpa))


# ------------------------------------------
# 4. Boolean (bool)
# ------------------------------------------

is_student = True
has_job = False

print("\nIs Student:", is_student)
print("Has Job:", has_job)
print("Boolean Data Type:", type(is_student))


# Boolean with comparison
is_adult = age >= 18

print("Is Adult:", is_adult)


# ------------------------------------------
# 5. List (list)
# ------------------------------------------

programming_languages = [
    "Python",
    "JavaScript",
    "C++"
]

print("\nProgramming Languages:", programming_languages)
print("First Language:", programming_languages[0])
print("List Data Type:", type(programming_languages))


# List can be changed
programming_languages[2] = "Java"

print("Updated Languages:", programming_languages)


# ------------------------------------------
# 6. Tuple (tuple)
# ------------------------------------------

coordinates = (23.8103, 90.4125)

print("\nCoordinates:", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])
print("Tuple Data Type:", type(coordinates))


# ------------------------------------------
# 7. Set (set)
# ------------------------------------------

numbers = {1, 2, 3, 3, 4, 4, 5}

print("\nSet:", numbers)
print("Set Data Type:", type(numbers))


# ------------------------------------------
# 8. Dictionary (dict)
# ------------------------------------------

student = {
    "name": "Hedaetullah",
    "age": 25,
    "department": "Software Engineering",
    "cgpa": 3.81
}

print("\nStudent Information:")
print(student)

print("Student Name:", student["name"])
print("Student Department:", student["department"])
print("Student CGPA:", student["cgpa"])

print("Dictionary Data Type:", type(student))


# ------------------------------------------
# 9. None (NoneType)
# ------------------------------------------

result = None

print("\nResult:", result)
print("Result Data Type:", type(result))


# ------------------------------------------
# 10. Type Conversion
# ------------------------------------------

# String to Integer
age_text = "25"
age_number = int(age_text)

print("\nAge as String:", age_text)
print("Age as Integer:", age_number)
print("Converted Data Type:", type(age_number))


# Integer to String
number = 100
number_text = str(number)

print("\nNumber:", number)
print("Number as String:", number_text)
print("Converted Data Type:", type(number_text))


# String to Float
price_text = "99.50"
price = float(price_text)

print("\nPrice as String:", price_text)
print("Price as Float:", price)
print("Converted Data Type:", type(price))


# Integer to Float
marks = 80
marks_float = float(marks)

print("\nMarks:", marks)
print("Marks as Float:", marks_float)
print("Converted Data Type:", type(marks_float))


# ------------------------------------------
# 11. Checking Multiple Data Types
# ------------------------------------------

data1 = "Python"
data2 = 100
data3 = 10.5
data4 = True
data5 = [1, 2, 3]
data6 = (1, 2, 3)
data7 = {1, 2, 3}
data8 = {"name": "Hedaetullah"}

print("\n========== Data Type Summary ==========")

print(data1, "->", type(data1))
print(data2, "->", type(data2))
print(data3, "->", type(data3))
print(data4, "->", type(data4))
print(data5, "->", type(data5))
print(data6, "->", type(data6))
print(data7, "->", type(data7))
print(data8, "->", type(data8))