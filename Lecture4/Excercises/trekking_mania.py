n = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
total_count = 0

for i in range(n):
    people_count = int(input())
    total_count += people_count
    if people_count >= 41:
        group5 += people_count
    elif people_count >= 26:
        group4 += people_count
    elif people_count >= 13:
        group3 += people_count
    elif people_count >= 6:
        group2 += people_count
    else:
        group1 += people_count


group1_percent = group1 / total_count * 100
group2_percent = group2 / total_count * 100
group3_percent = group3 / total_count * 100
group4_percent = group4 / total_count * 100
group5_percent = group5 / total_count * 100

print(f"{group1_percent:.2f}%")
print(f"{group2_percent:.2f}%")
print(f"{group3_percent:.2f}%")
print(f"{group4_percent:.2f}%")
print(f"{group5_percent:.2f}%")