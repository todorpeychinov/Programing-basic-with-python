a = int(input())
b = int(input())
operation = input()

result = None

if operation == "+" or operation == "-" or operation == "*":
    math_result = eval(f"{a} {operation} {b}")
    result = f"{a} {operation} {b} = {math_result}"
    result += (" - even" if math_result % 2 == 0 else " - odd")

elif b == 0:
    result = f"Cannot divide {a} by zero"

elif operation == "/":
    math_result = eval(f"{a} {operation} {b}")
    result = f"{a} {operation} {b} = {math_result:.2f}"

elif operation == "%":
    math_result = eval(f"{a} {operation} {b}")
    result = f"{a} {operation} {b} = {math_result}"

print(result)
