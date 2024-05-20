from math import floor
record = float(input())
distance = float(input())
time = float(input())

seconds_to_swim = distance * time
extra_seconds = floor((distance / 15)) * 12.5

ivans_time = seconds_to_swim + extra_seconds

if ivans_time < record:
    print(f"Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.")

else:
    extra_time = ivans_time - record
    print(f"No, he failed! He was {extra_time:.2f} seconds slower.")
