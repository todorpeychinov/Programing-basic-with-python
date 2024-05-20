trainers = int(input())
grades_sum = 0
grades_count = 0

while True:
    presentation = input()

    if presentation == "Finish":
        print(f"Student's final assessment is {grades_sum / grades_count:.2f}.")
        break

    current_grades = 0
    for i in range(trainers):
        current_grades += float(input())

    grades_sum += current_grades
    grades_count += trainers
    print(f"{presentation} - {current_grades / trainers:.2f}.")


