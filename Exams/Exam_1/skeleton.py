control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_for_one_hundred_meters = int(input())

control_seconds += control_minutes * 60

minus_time = (length / 120) * 2.5

total_time = (length / 100) * seconds_for_one_hundred_meters - minus_time

if total_time <= control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")

else:
    print(f"No, Marin failed! He was {total_time - control_seconds:.3f} second slower.")


