pages = int(input())
pages_for_hour = int(input())
days_number = int(input())

total_reading_time = pages // pages_for_hour
time_for_day = total_reading_time // days_number

print(time_for_day)