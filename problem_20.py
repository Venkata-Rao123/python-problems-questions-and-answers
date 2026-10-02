# nested list 
n = int(input("Enter the number of students: "))
student = []
for i in range(n):
    name = input("Enter the name: ")
    score = float(input("Enter the score: "))
    student.append([name,score])
grades = []
for s in student:
    grades.append(s[1])
unique_grades = sorted(set(grades))
second_grade = unique_grades[1]
names = []
for s in student:
    if s[1] == second_grade:
        names.append(s[0])
names.sort()
for name in names:
    print(name)
    



n = int(input("Enter the number of students: "))
student = []
for i in range(n):
    name = input("Enter the name: ")
    score = int(input("Enter the marks: "))
    student.append([name,score])
grade = []
for s in student:
    grade.append(s[1])
unique_grades = sorted(tuple(grade))
second_grade = unqiue_grades[1]
names = []
for s in student:
    if s[1] == second_grade:
        names.append(s[0])
names.sort()
for name in names:
    print(name)

    












'''Store student details: Create a nested list containing each student's name and grade.

Extract grades: Collect all grades into a separate list.

Find unique grades: Use set() to remove duplicate grades.

Sort grades: Use sorted() to arrange the unique grades in ascending order.

Find the second lowest: Select unique_grades[1].

Find matching students: Collect the names of students whose grades equal the second-lowest grade.

Sort names: Arrange the names alphabetically.

Print names: Print each name on a separate line.'''
