daytime = int(input())
day_of_week = input()

result = "closed"

if day_of_week != "Sunday" and  10 <= daytime <= 18:
    result = "open"

print(result)