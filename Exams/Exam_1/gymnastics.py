country = input()
tool = input()
points = 0

if country == "Russia":

    if tool == "ribbon":
        points = 9.1 + 9.4
    elif tool == "hoop":
        points = 9.3 + 9.8
    elif tool == "rope":
        points = 9.6 + 9

elif country == "Bulgaria":

    if tool == "ribbon":
        points = 9.6 + 9.4
    elif tool == "hoop":
        points = 9.55 + 9.75
    elif tool == "rope":
        points = 9.5 + 9.4

elif country == "Italy":

    if tool == "ribbon":
        points = 9.2 + 9.5
    elif tool == "hoop":
        points = 9.45 + 9.35
    elif tool == "rope":
        points = 9.7 + 9.1

print(f"The team of {country} get {points:.3f} on {tool}.")
print(f"{(20 - points) / 20 * 100:.2f}%")