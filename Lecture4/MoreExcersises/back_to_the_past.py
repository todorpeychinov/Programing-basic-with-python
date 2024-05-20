ivan_years = 18

heritage = float(input())
years = int(input()) - 1800

for i in range(0, years + 1):
    if i % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + 50 * ivan_years
    ivan_years += 1

if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage):.2f} dollars to survive.")



