juniors_count = int(input())
seniors_count = int(input())
race_type = input()

juniors_tax = 0
seniors_tax = 0
total_sum = 0


if race_type == "trail":
    juniors_tax = juniors_count * 5.5
    seniors_tax = seniors_count * 7
    total_sum = juniors_tax + seniors_tax
elif race_type == "cross-country":
    juniors_tax = juniors_count * 8
    seniors_tax = seniors_count * 9.5
    total_sum = juniors_tax + seniors_tax
    if juniors_count + seniors_count >= 50:
        total_sum -= total_sum * 0.25
elif race_type == "downhill":
    juniors_tax = juniors_count * 12.25
    seniors_tax = seniors_count * 13.75
    total_sum = juniors_tax + seniors_tax
elif race_type == "road":
    juniors_tax = juniors_count * 20
    seniors_tax = seniors_count * 21.5
    total_sum = juniors_tax + seniors_tax


total_sum -= total_sum * 0.05


print(f"{total_sum:.2f}")
