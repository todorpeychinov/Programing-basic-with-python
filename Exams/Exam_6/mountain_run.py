from math import floor

record = float(input())
meters = float(input())
seconds_per_meter = float(input())

plus_time = floor(meters / 50) * 30

georgi_time = meters * seconds_per_meter + plus_time

if georgi_time < record:
    print(f"Yes! The new record is {georgi_time:.2f} seconds.")
else:
    print(f"No! He was {georgi_time - record:.2f} seconds slower.")

