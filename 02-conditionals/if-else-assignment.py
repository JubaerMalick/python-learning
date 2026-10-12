'''
Create a variable (grade) holding an integer between 0 - 100
Code if, elif, else statement to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70 -79
D = 60 - 69
F = 0 - 59
'''

grade = int(input("Enter your grade : "))


if (grade >= 90):
    print("Your Grade is : A")
elif (grade >= 80 and grade <= 89 ):
    print("Your Grade is : B")
elif (grade >= 70 and grade <= 79 ):
    print("Your Grade is : C")
elif (grade >= 60 and grade <= 69 ):
    print("Your Grade is : D")
else:
    print("Your Grade is : F")