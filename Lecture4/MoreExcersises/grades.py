students_count = int(input())
top_students = 0
good_students = 0
middle_students = 0
fail_students = 0
average = 0

for i in range(students_count):
    grade = float(input())
    average += grade
    if grade >= 5:
        top_students += 1
    elif grade >= 4:
        good_students += 1
    elif grade >= 3:
        middle_students += 1
    else:
        fail_students += 1

average_grade = average / students_count

percent_top_students = top_students / students_count * 100
percent_good_students = good_students / students_count * 100
percent_middle_students = middle_students / students_count * 100
percent_fail_students = fail_students / students_count * 100

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_middle_students:.2f}%")
print(f"Fail: {percent_fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")



