deposit = float(input())
months = int(input())
increase_percent = float(input()) / 100

total_sum = deposit + months * ((deposit * increase_percent) / 12)

print(total_sum)