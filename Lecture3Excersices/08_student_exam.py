exam_hours = int(input())
exam_minutes = int(input())
student_hours = int(input())
student_minutes = int(input())

exam_in_minutes = exam_hours * 60 + exam_minutes
student_in_minutes = student_hours * 60 + student_minutes

time_dif = exam_in_minutes - student_in_minutes

if time_dif > 30:
    print("Early")

elif time_dif < 0:
    print("Late")

else:
    print(f"On time")

hours = abs(time_dif) // 60
minutes = abs(time_dif) % 60

result = ""

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_dif > 0:
    result += " before the start"
elif time_dif < 0:
    result += " after the start"

print(result)
