number_of_grades = int(input())
average = 0
count_of_grades = 0
fails = 0

while True:
    user_input = input()
    if user_input == "Enough":
        print(f"Average score: {average / count_of_grades:.2f}")
        print(f"Number of problems: {count_of_grades}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    average += grade
    count_of_grades += 1
    if grade <= 4:
        fails += 1
        if fails == number_of_grades:
            print(f"You need a break, {fails} poor grades.")
            break
    last_problem = user_input

