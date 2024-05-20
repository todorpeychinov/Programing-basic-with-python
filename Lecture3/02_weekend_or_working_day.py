day_of_week = input()
output = " "

if day_of_week == "Monday" or day_of_week == "Tuesday" \
    or day_of_week == "Wednesday" or day_of_week == "Thursday" \
    or day_of_week == "Friday":
    output = "Working day"
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    output = "Weekend"
else:
    output = "Error"

print(output)