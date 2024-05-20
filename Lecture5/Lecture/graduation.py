name = input()
fails = 0
average = 0
grade = 0
student_class = 1

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            print(f"{name} has been excluded at {student_class} grade")
            break
        else:
            continue
    average += grade
    student_class += 1
    if student_class > 12:
        break

if student_class >= 12:
    print(f"{name} graduated. Average grade: {average / 12 :.2f}")
