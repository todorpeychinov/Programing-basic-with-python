town = input()
turnover = float(input())
result = "error"

if town == "Sofia":
    if  0 <= turnover <= 500:
        result = turnover * 0.05
    elif 500 < turnover <= 1000:
        result = turnover * 0.07
    elif 1000 < turnover <= 10000:
        result = turnover * 0.08
    elif turnover > 10000:
        result = turnover * 0.12
elif town == "Varna":
    if  0 <= turnover <= 500:
        result = turnover * 0.045
    elif 500 < turnover <= 1000:
        result = turnover * 0.075
    elif 1000 < turnover <= 10000:
        result = turnover * 0.1
    elif turnover > 10000:
        result = turnover * 0.13
elif town == "Plovdiv":
    if 0 <= turnover <= 500:
        result = turnover * 0.055
    elif 500 < turnover <= 1000:
        result = turnover * 0.08
    elif 1000 < turnover <= 10000:
        result = turnover * 0.12
    elif turnover > 10000:
        result = turnover * 0.145

if result != "error":
    print(f"{result:.2f}")
else:
    print(result)


